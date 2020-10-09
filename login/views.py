from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Client,Manager
from information.models import *
from django.contrib import  auth
# Create your views here.

# def re(response):
#     return  response
def index(request):
    if request.method == "GET":
        username = '用户名'
        passwords = '密码'
        values = '/'
        return render(request,'login/login.html',{'username':username,'passwords':passwords,'values':values})
    else:
        username = request.POST.get('username', '')
        passwords = request.POST.get('passwords', '')
        isc = False
        user = ''
        for c in Client.objects.all():
            if c.cname == username:
                user = c
                isc = True

        if user == '':
            for m in Manager.objects.all():
                if m.mname == username:
                    user = m
        if user =='':
            passwords = '密码'
            values = '/'
            return render(request,'login/login.html', {'username':username,'passwords':passwords,'values':values})
        elif isc:
            if user.cpasswords == passwords:
                response = HttpResponseRedirect('/mainpage')
                response.set_cookie('username',username)
                response.set_cookie('state', 'client')
                # response.set_cookie('isentertainment', 1)
                return response
                # re(response)
                # return render(request,'managerpage/managerpage.html',{'isentertainment':1})
            else:
                passwords = '密码错误'
                values = username
                username = '用户名'
                return render(request,'login/login.html',
                              {'username':username,'passwords':passwords,'values':values})
        else:
            if user.mpasswords == passwords:
                manager = Manager.objects.get(mname=username)
                house = ManagerHouse.objects.get(manager=manager.pk).house
                category = house.hcategory
                isentertainment = 1 if category == '娱乐场所' else 0
                response = HttpResponseRedirect('/managerpage')
                response.set_cookie('username', username)
                response.set_cookie('state', 'manager')
                response.set_cookie("isentertainment",isentertainment)
                return response
            else:
                passwords = '密码错误'
                values = username
                username = '用户名'
                return render(request, 'login/login.html',
                              {'username': username, 'passwords': passwords, 'values': values})

def register(request):
    if request.method == "GET":
        username = '用户名'
        passwords1 = '密码'
        passwords2 = '密码'
        gender = '性别'
        age = '年龄'
        email = '邮箱'
        phonenum = '号码'
        state = '身份'
        return render(request, 'login/register.html',
                      {'username': username, 'passwords1': passwords1, 'passwords2': passwords2, 'gender': gender,
                       'age': age, 'email': email, 'phonenum': phonenum, 'state': state})
    else:
        username =  request.POST.get('username', '')
        passwords1 = request.POST.get('passwords1','')
        passwords2 = request.POST.get('passwords2','')
        gender = request.POST.get('gender','')
        age = request.POST.get('age','')
        email = request.POST.get('email','')
        phonenum = request.POST.get('phonenum','')
        # state = request.POST.get('state','')
        if username == '' or passwords1 == '' or passwords2 == '' or age == '' or email == '' or phonenum == '' or passwords2 != passwords1:
            return render(request,'login/register.html',{'username':username,'passwords1':passwords1,'passwords2':passwords2,'gender':gender,
                                                         'age':age,'email':email,'phonenum':phonenum})

        try:
            c = Client(cname=username,cpasswords=passwords1,cgender=gender,cage=age,cemail=email,cphonenum=phonenum)
            c.save()
        except:
            return render(request, 'login/register.html',
                          {'username': '用户名已被占用', 'passwords1': passwords1, 'passwords2': passwords2,
                           'gender': gender,
                           'age': age, 'email': email, 'phonenum': phonenum})
        # else:
        #     try:
        #         m = Manager(mname=username, mpasswords=passwords1, mgender=gender, mage=age, memail=email, mphonenum=phonenum)
        #         m.save()
        #     except:
        #         return render(request, 'login/register.html',
        #                       {'username': '用户名已被占用', 'passwords1': passwords1, 'passwords2': passwords2,
        #                        'gender': gender,
        #                        'age': age, 'email': email, 'phonenum': phonenum, 'state': state})
        return render(request, 'login/register_success.html')
