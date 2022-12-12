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
            
            if x.email==umail and x.password==pswd:
              
                request.session['uid']=x.userid
                return redirect('/home/')
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

def home(request):
    user_id=request.session['uid']
    todays_date = date.today()
    month1 = todays_date.month
    year1=todays_date.year 
    res=Reservations.objects.filter(userid=int(user_id),month=month1,year=year1)
    if len(res)>0:
        user=User.objects.filter(userid=user_id)
        d1={}
        for x in user:
            d1['name']=x.name
            d1['email']=x.email 
            d1['phn']=x.phno 
            d1['age']=x.age 

        for x in res:
            d1['batch']=x.batch 
        print(d1)
        data={
        'context':d1
        }   
        return render(request,"home.html",data)
    else:
        if request.method=='POST':
            x=len(Reservations.objects.all())
            todays_date = date.today()
            month1 = todays_date.month
            year1=todays_date.year
            Reservations.objects.create(userid=int(user_id),resid=x+1,payamount=500,batch=request.POST['batch'],month=month1,year=year1)
            return redirect("/home/")
        return render(request,"expired.html")
    

    
    
        





