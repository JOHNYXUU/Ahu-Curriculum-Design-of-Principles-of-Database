from django.shortcuts import render
from .models import *
from login.models import  Client
from django.http import HttpResponse,HttpResponseRedirect
import pytz
import random
# Create your views here.

def mainpage(request):
    return render(request,'mainpage/mainpage.html')

def information(request,category):
    wares = []
    cate = ''
    if category == 'logout':
        res = HttpResponseRedirect('/login')
        res.delete_cookie('username')
        return res
    if category == 'profile':
        username = request.COOKIES.get('username','')
        return HttpResponse(username)
    if category == 'changeorder':
        if request.method == 'GET':
            username = request.COOKIES.get('username', '')
            user = Client.objects.get(cname=username)
            orders = WareOrder.objects.filter(WOclient=user.id)
            return  render(request,"information/change_order.html",{'orders':orders})
        else:
            order_id = int(request.POST.get('selected', '').replace('-','').split()[0][4:])
            operate = request.POST.get('operate', '')
            order = WareOrder.objects.get(pk=order_id)
            if operate == 'cancel':
                ware = order.WOware
                ware.wnum += order.WOnum
                ware.wsalenum -= order.WOnum
                ware.save()
                order.delete()
                operate = '订单取消'
                return render(request,'information/changeorder_success.html',{"operate":operate})
            else:
                operate = '订单修改'
                try:
                    num = int(request.POST.get('number',''))
                except:
                    num = order.WOnum
                print(num)
                last_num = order.WOnum
                print(last_num)
                ware = order.WOware
                ware.wsalenum += (num - last_num)
                ware.wnum += (last_num - num)
                ware.save()
                order.WOnum = num
                address = request.POST.get('address','')
                if address != '':
                    order.WOaddress = address
                order.save()
                return render(request, 'information/changeorder_success.html', {"operate": operate,'order':order})

    if category == 'warehouse' :
        emptys = []
        entertainments = []
        storages = []
        for warehouse in Warehouse.objects.all():
            if warehouse.hisoccupied == False:
                emptys.append(warehouse)
            elif warehouse.hcategory == '娱乐场所':
                entertainments.append(warehouse)
            else:
                storages.append(warehouse)
        return render(request, 'information/warehouselist.html',
                      {'emptys': emptys, 'entertainments': entertainments, 'storages': storages})
    else:
        for w in Ware.objects.all():
            if category=='eleapp' and w.wcategory == '电器':
                wares.append(w)
                cate = '电器'
            if category == 'digital' and w.wcategory == '数码':
                wares.append(w)
                cate = '数码'
            if category=='food' and w.wcategory == '食品':
                wares.append(w)
                cate = '食品'
            if category=='book' and w.wcategory == '图书':
                wares.append(w)
                cate = '图书'
        return  render(request,'information/warelist.html',{'category':cate,'wares':wares})

def waredetail(request,category,name):
    if request.method == "GET":
        if name == 'changeorder':
            return render(request, "information/service/change_order.html")

        if category == 'warehouse':
            warehouse = Warehouse.objects.get(hname = name)
            if warehouse.hisoccupied == False:
                return render(request,"information/warehouse.html",{'warehouse':warehouse})
            else:
                fromdate = HouseOrder.objects.get(HOhouse=warehouse.pk).HOfromdate
                m = HouseOrder.objects.get(HOhouse=warehouse.pk).HOduration
                now = datetime.datetime.now()
                now = now.replace(tzinfo=pytz.timezone('UTC'))
                months =  (now-fromdate).days / 30
                month = int(m - months + 0.5)
                return render(request, "information/warehouse_rented.html", {'warehouse': warehouse,'month':month})
        # ware = Ware()
        if category == 'eleapp' or category == 'food' or category == 'book' or category == 'digital':
            ware = Ware.objects.get(wname=name)
            location = HouseWare.objects.get(wares_id=ware.pk).house.hlocation
            return render(request,"information/ware.html",{'ware':ware,'location':location})
    else:
        username = request.COOKIES.get('username', '')
        if category == 'eleapp' or category == 'food' or category == 'book' or category == 'digital':
            ware = Ware.objects.get(wname=name)
            client = Client.objects.get(cname=username)
            num = request.POST.get('amount', '')
            address = request.POST.get('address', '')
            location = HouseWare.objects.get(wares_id=ware.pk).house.hlocation
            order = WareOrder(WOclient=client,WOware=ware,WOnum=num,WOaddress=address)
            order.save()
            ware.wsalenum += int(num)
            ware.wnum -= int(num)
            ware.save()
            return  render(request,"information/waresuccess.html",{'ware':ware,'location':address,'num':num})

        if category == 'warehouse':
            warehouse = Warehouse.objects.get(hname=name)
            client = Client.objects.get(cname=username)
            month = request.POST.get('amount', '')
            order = HouseOrder(HOhouse=warehouse,HOclient=client,HOduration=month)
            order.save()
            warehouse.hisoccupied = True
            warehouse.hpurpose = request.POST.get('detail', '')
            warehouse.hcategory = request.POST.get('category', '')
            warehouse.save()
            manager = ManagerHouse.objects.get(house=warehouse.pk).manager
            newcode = ''
            for i in range(6):
                newcode += str(random.randint(0,9))
            manager.mpasswords = newcode
            manager.save()
            return render(request,"information/warehouse_success.html",{'manager':manager})
