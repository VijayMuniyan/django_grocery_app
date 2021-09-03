from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Grocery



def home(request):
    return render(request,"home.html")
def registration(request):
    if request.method=='POST':
        username=request.POST.get("username")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        print(firstname)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                #print("username already exists")
                return redirect("registration")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exists")
                #print("email already exists")
                return redirect("registration")
            else:
                user=User.objects.create_user(username=username,first_name=firstname,email=email,password=password1)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"Password is not match")
            #print("Password is not match")
            return redirect("registration")
    else:
        return render(request,"registration.html")

def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("add")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")

    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect("last")
def last(request):
    return render(request,"last.html")



def add(request):


        if request.method=='POST':

                Item_name=request.POST.get('Item_name')
                print(Item_name)
                Item_quantity=int(request.POST.get('Item_quantity'))
                print(Item_quantity)
                Item_status=request.POST.get('Item_status')
                print(Item_status)
                datetime=request.POST.get('datetime')
                print(datetime)
                obj=Grocery.objects.create(Item_name=Item_name, Item_quantity=Item_quantity, Item_status=Item_status, Date=datetime)
                obj.save()
                return redirect('details')


        return render(request,'add.html')


def update(request,i):
        #data=Grocery.objects.filter(Item_name=i)

        if request.method=='POST':

                Item_name=request.POST.get('Item_name')
                print(Item_name)
                Item_quantity=int(request.POST.get('Item_quantity'))
                print(Item_quantity)
                Item_status=request.POST.get('Item_status')
                print(Item_status)
                datetime=request.POST.get('datetime')
                print(datetime)
                obj=Grocery.objects.filter(Item_name=i).update(Item_name=Item_name, Item_quantity=Item_quantity, Item_status=Item_status, Date=datetime)
                #obj.save()
                return redirect('details')

        return render(request,'update.html')


def details(request):
    data=Grocery.objects.all()
    query=request.GET.get("search")
    if query is not None:
        data=data.filter(Date=query)
    return render(request,"details.html",{"data":data})
