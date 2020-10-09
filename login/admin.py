from django.contrib import admin
from .models import Client,Manager
# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    #列表页属性
    list_display = ['pk','cname','cgender','cage','cemail','cphonenum','cpasswords']
    list_filter = ['cname'] #过滤器
    search_fields = ['cname'] #搜索字段
    list_per_page = 20 #分页

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['pk','mname','mpasswords']
    list_filter = ['mname'] #过滤器
    search_fields = ['mname'] #搜索字段
    list_per_page = 20 #分页