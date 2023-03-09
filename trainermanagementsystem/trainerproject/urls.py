"""trainermanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.urls import path

from trainerapp import views

urlpatterns=[
    path('register',views.reg_fun,name='register'), #it will display register.html
    path('regdata',views.reg_data_fun), #it will store the data either in User table or in reg table
    path('log',views.log_fun,name='log'), #it will display login.html
    path('logread',views.log_read_fun), #it will
    path('Ahome', views.admin_home_fun, name='Ahome'), #display Admin homepage
    path('Thome', views.trainer_home_fun, name='Thome'), #it will display Trainer Homepage
    path('trainer_details',views.trainer_details, name='trainer_details'),# it will display all the trainer details
    path('delete/<int:x>',views.delete_fun,name='delete'),#it will particular trainer details
    path('batch_Assign', views.batch_data_fun,name='batch_Assign'),
    path('readdata',views.batch_assign_fun),
    path('batchdetails',views.batch_details, name='batchdetails'),
    path('log_out',views.logout_fun,name='log_out')


]

