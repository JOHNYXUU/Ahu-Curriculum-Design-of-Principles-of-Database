from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from information.models import *
from login.models import *
# Create your views here.

def managerpage(request):
    return render(request,'managerpage/managerpage.html')

def functions(request,function):
    username = request.COOKIES.get('username', '')
    manager = Manager.objects.get(mname=username)
    house = ManagerHouse.objects.get(manager=manager.pk).house
    name = house.hname
    if function == 'visitorflow':
        if house.hcategory == '货物存储':
            return HttpResponse("storage warehouse doesn't have this function")
        else:
            visitorFlowData = Visitorflow.objects.filter(Vhouse=house.id)
            date = []
            num = []
            for data in visitorFlowData:
                date.append(str(data.Vdate.strftime("%m-%d")))
                num.append(data.Vnum)
            return render(request,"managerpage/visitorflow.html",{'date':date,'num':num,'name':name})
    if function == 'monitor':
        return HttpResponse(function)

    if house.hcategory == '娱乐场所':
        return HttpResponse("entertainment warehouse doesn't have this function")
    else:
        HW = HouseWare.objects.filter(house=house.pk)
        num = []
        names = []
        if function == 'inoutput':
            for W in HW:
                num.append(W.wares.wnum)
                names.append(W.wares.wname)
            if request.method == 'GET':
                return render(request, 'managerpage/inoutput.html', {'num': num, 'names': names, 'name': name})
            else:
                operation = ''
                num = []
                names = []
                selected = request.POST.get('selected', '').replace('-','')
                inorout = request.POST.get('operate', '')
                number = request.POST.get('number', '')
                try:
                    number = int(number)
                except:
                    number = 0
                ware = Ware.objects.get(wname=selected)
                if inorout == 'in':
                    operation = '进货'
                    ware.wnum += number
                else:
                    operation = '出货'
                    ware.wnum -= number
                ware.save()
                for W in HW:
                    num.append(W.wares.wnum)
                    names.append(W.wares.wname)
                return render(request, 'managerpage/inoutputsuccess.html', {'ware': ware, 'num':number,'operation':operation})
        if function == 'salestatic':
            for W in HW:
                num.append(W.wares.wsalenum)
                names.append(W.wares.wname)
            return render(request,'managerpage/salestatic.html',{'num':num,'names':names,'name':name})
        if function == 'warestatic':
            for W in HW:
                num.append(W.wares.wnum)
                names.append(W.wares.wname)
            return render(request,'managerpage/storagestatic.html',{'num':num,'names':names,'name':name})