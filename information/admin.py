from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
@admin.register(Ware)
class WareAdmin(admin.ModelAdmin):

    #列表页属性
    list_display = ['pk','wname','wnum','wsalenum','wcategory','wprice','wdescription']
    list_filter = ['wname'] #过滤器
    search_fields = ['wname'] #搜索字段

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = ['pk','hname','hlocation','harea','hprice','hisoccupied','hpurpose','hcategory','hphoto']
    list_filter = ['hname'] #过滤器
    search_fields = ['hname'] #搜索字段

@admin.register(WareOrder)
class WareOrderAdmin(admin.ModelAdmin):

    list_display = ['pk','WOware','WOclient','WOnum','WOdate','WOaddress']
    list_filter = ['WOclient'] #过滤器
    search_fields = ['WOclient'] #搜索字段

@admin.register(HouseOrder)
class HouseOrderAdmin(admin.ModelAdmin):

    list_display = ['pk','HOhouse','HOclient','HOfromdate','HOduration']
    list_filter = ['HOclient'] #过滤器
    search_fields = ['HOclient'] #搜索字段

@admin.register(Visitorflow)
class VisitorflowAdmin(admin.ModelAdmin):

    list_display = ['pk','Vhouse','Vdate','Vnum']
    list_filter = ['Vhouse'] #过滤器
    search_fields = ['Vhouse'] #搜索字段

@admin.register(HouseWare)
class HouseWareAdmin(admin.ModelAdmin):

    list_display = ['pk','house','wares']

@admin.register(ManagerHouse)
class ManagerHouseAdmin(admin.ModelAdmin):

    list_display = ['pk','manager','house']