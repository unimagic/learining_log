"""为应用程序users定义URL模式"""
from telnetlib import LOGOUT
from unicodedata import name
from django.urls import re_path as url
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from . import views

urlpatterns=[
    #登录界面
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    #注销界面
    url(r'^logout/$',views.logout_view,name='logout'),
    #注册页面
    url(r'^register/$',views.register,name='register')
]