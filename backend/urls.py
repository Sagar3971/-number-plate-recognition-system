from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home1, name='home1'),
    path('joinnow',views.joinnow, name='joinnow'),
    path('account',views.account, name='account'),
    path('loginpage',views.loginpage, name='loginpage'),
    path('trafficrules',views.trafficrules, name='trafficrules'),
    path('search',views.search, name='search'),
    path('userfound',views.userfound, name='userfound'),
    path('usernotfound',views.usernotfound, name='usernotfound'),  
    path('upload',views.upload, name='upload'),
    path('scan',views.scan, name='realscan'),     
]