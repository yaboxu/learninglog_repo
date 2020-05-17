"""定义应用程序users的URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [   
    #登录页面，没有编写视图函数而是传递了一个字典
    url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'), 
    
    #注销 logout_view()区分logout()
    url(r'^logout/$', views.logout_view, name='logout'), 
    
    #注册页面
    url(r'^register/$', views.register, name='register'), 
   
    ]
