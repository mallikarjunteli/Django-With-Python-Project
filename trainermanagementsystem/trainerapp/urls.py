from django.urls import path

from trainerapp import views

urlpatterns = [
    path('reg',views.reg_fun,name='reg'),# it will display register page.html output
    path('reg_data',views.reg_data_fun), # it will store the data either in user table nor in trainer reg table
    path('log',views.log_fun,name='log'), # it will display login html file
    path('logread',views.logread_fun) # it will read dataa and login to the particular page
]