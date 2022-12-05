from django.shortcuts import render, redirect
from .models import blog
from .forms import django_form
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def show(request):  
    d=blog.objects.all()
    return render (request,'show.html',{'d':d})

@login_required(login_url='login')
def djangof(request):
    if request.method == 'GET':
        form = django_form()
        return render(request,'new.html',{'form':form})
    else:
        form=django_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
        
        # else:
        #     return redirect('show')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['password2']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"*Your password does not match with confirm password")
            return redirect('signup')

    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('show')
        else:
            messages.info(request,"*Your password does not match with Username")
            return render(request,'front.html')
    return render(request,'front.html')
    



def logout(request):
    auth.logout(request)
    return redirect('login')


def delete(request,id):
    d = blog.objects.get(id=id)
    d.delete()
    return redirect('show')

@login_required(login_url='login')
def update(request,id):
    d = blog.objects.get(id = id)
    if request.method == 'GET':
        form = django_form(instance=d)
        return render (request,'new.html',{'form':form})
    else:
        form=django_form(request.POST,request.FILES,instance=d)
        if form.is_valid():
            form.save()
            return redirect('show')


def about(request):
    return render(request,'about.html')