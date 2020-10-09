from django.db import models
# from dateutil.relativedelta import relativedelta
from login.models import  Client,Manager
import django.utils.timezone as timezone
import datetime
# Create your models here.

class Ware(models.Model):
    def __str__(self):
        return  self.wname
    eleapp = '电器'
    digital = '数码'
    food = '食品'
    book = '图书'
    wname = models.CharField(max_length=50)
    wcategory = models.CharField(max_length=10,choices=[(eleapp,'电器'),(digital,'数码'),(food,'食品'),(book,'图书')])
    wnum = models.IntegerField(default=0)
    # wmeasureunit = models.CharField(max_length=5)
    wprice = models.FloatField(default=0)
    # wstandards = models.CharField(max_length=5)
    # whouse = models.ForeignKey("Warehouse", on_delete=models.CASCADE,limit_choices_to={'hcategory':'货物存储'})
    wdetailphoto = models.ImageField(default='',blank=True,null=True,upload_to='')
    wlistphoto = models.ImageField(default='', blank=True, null=True, upload_to='')
    wsalenum = models.IntegerField(default=0)
    wdescription = models.CharField(default='',max_length=100,blank=True)

class Warehouse(models.Model):
    def __str__(self):
        return self.hname+' '+self.hpurpose

    storage = '货物存储'
    entertainment = '娱乐场所'
    tobedefined = ''
    hname = models.CharField(max_length=20,unique=True)
    hlocation = models.CharField(max_length=50)
    harea = models.IntegerField()
    hisoccupied = models.BooleanField(default=False)
    hpurpose = models.CharField(max_length=500,default='',blank=True)
    hcategory = models.CharField(default=False,choices=[(storage,'货物存储'),(entertainment,'娱乐场所'),(tobedefined,'')],max_length=4,blank = True)
    hphoto = models.ImageField(default='', blank=True, null=True, upload_to='')
    hprice = models.FloatField(default=20.0)

class WareOrder(models.Model):
    def __str__(self):
        return "订单号:"+str(self.pk)+' '+self.WOware.wname + ' '+ str(self.WOdate)[:19]
    WOware = models.ForeignKey(Ware,on_delete=models.CASCADE)
    WOclient = models.ForeignKey(Client,on_delete=models.CASCADE)
    WOnum = models.IntegerField(default=1)
    WOdate = models.DateTimeField(default=timezone.now)
    WOaddress = models.CharField(default='',max_length=100,blank=True)

class HouseOrder(models.Model):
    HOhouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE)#limit_choices_to={'hisoccupied':False}
    HOclient = models.ForeignKey(Client,on_delete=models.CASCADE)
    HOfromdate = models.DateTimeField(default=timezone.now)
    HOduration = models.IntegerField(blank=False)

class Visitorflow(models.Model):
    Vhouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE,limit_choices_to={'hcategory':'娱乐场所'})
    Vdate = models.DateField(blank=False)
    Vnum = models.IntegerField(default=0)

class HouseWare(models.Model):
    house = models.ForeignKey(Warehouse,on_delete=models.CASCADE,limit_choices_to={'hcategory':'货物存储'})
    wares = models.ForeignKey(Ware,on_delete=models.CASCADE,default=1)

class ManagerHouse(models.Model):
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE, default=6)
    house = models.OneToOneField(Warehouse,on_delete=models.CASCADE)
