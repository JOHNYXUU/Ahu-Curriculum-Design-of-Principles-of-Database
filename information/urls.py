from django.contrib import admin
from django.urls import path
from . import views
from .models import Ware,Warehouse

urlpatterns = [
    path('mainpage/<str:category>',views.information),
    path('mainpage/',views.mainpage,name = 'mainpage'),
    path('mainpage/<str:category>/<str:name>',views.waredetail),
]