from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import request, HttpResponse
from django.shortcuts import render, redirect

from trainerapp.models import City, Course, Trainer_Reg


# Create your views here.
def reg_fun(request):
    city_data = City.objects.values()
    course_data = Course.objects.value()
    data = {
        'city':city_data,
        'course':course_data

    }

    return  render(request,'register_page.html',data)


def reg_data_fun(password=None):
    username = request.POST['txtName']
    userage = request.POST['txtAge']
    userphno = request.POST['txtPhno']
    useremail =request.POST['txtMail']
    userpswd = request.POST['txtPswd']
    usercity = request.POST['ddlcity']
    usercourse = request.POST['ddlcourse']
    usertype = request.POST['rdUserType']
    if usertype =='Admin':
        u1 = User.objects.create_superuser(username=username,password=password,email=useremail)
        u1.save()
        return HttpResponse('Super user Created Successfully')
    elif usertype == 'Trainer':
        t1 = Trainer_Reg()
        t1.Tname = username
        t1.Tage = userage
        t1.Tphno = userphno
        t1.Temail = useremail
        t1.Tpassword = userpswd
        t1.Tcity= City.objcets.get(city_name=usercity)
        t1.Tcourse = Course.objects.get(course_name = usercourse)
        t1.save()
        return HttpResponse('Trainer data Created Successfully')
    else:
        return redirect('reg',{'data': 'enter proper data'})


def log_fun(request):
    return render(request,'login_page.html',{'data':''})


def logread_fun(request):
    user_name = request.POST['txtUseName']
    user_pswd = request.POST['txttxtPswd']
    user1 = authenticate(username=user_name,password=user_pswd)
    if user1 is not None:
        if user1.is_superuser:
            return render(request,'adminhome.html')
    elif Trainer_Reg.objects.filter(Tname = user_name,Tpassword=user_pswd)

    return None