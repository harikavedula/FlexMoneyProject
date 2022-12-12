from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
from datetime import date

def login(request):
    if request.method=='POST':
        umail=request.POST['email']
        pswd=request.POST['pswd']
        user=User.objects.all()
        print(user)
        for x in user:
            # print(x.email)
            # print(x.password)
            # print(x.age)
            # print(x.name)
            if x.email==umail and x.password==pswd:
              
                request.session['uid']=x.name
                return redirect('home/')
        else:
            return HttpResponse("WRONG CREDENTIALS")
    return render(request, "login.html")

def register(request):
    if request.method=='POST':
        umail=request.POST['email']
        users=User.objects.filter(email=umail)
        print(len(users))
        if len(users)>0:
            return HttpResponse("USER ALREADY EXISTS , PLEASE LOGIN !!!")
        else:
            users1=User.objects.filter()
            n=len(users1)
            pswd=request.POST['pswd']
            uname=request.POST['name']
            phno=request.POST['phone']
            age=request.POST['age']
            batch=request.POST['batch']
            User.objects.create(name=uname,userid=n+1,email=umail,phno=phno,age=age,password=pswd)
            n1=len(Reservations.objects.filter())
            todays_date = date.today()
            month1 = todays_date.month
            year1=todays_date.year
            Reservations.objects.create(resid=n1+1,userid=n+1,payamount=500,batch=batch,month=month1,year=year1)
        print(len(User.objects.filter()))
        return redirect('/')



