from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('managerpage/',views.managerpage),
    path('managerpage/<str:function>',views.functions)
]