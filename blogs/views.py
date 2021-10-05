from os import name
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import signUp,loginForm,adddata
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group,User
from django.core.cache import cache

def home(request):
    posts=Post.posts.all() 
    return render(request, 'enroll/home.html',{'posts':posts}) 


def about(request):
    return render(request, 'enroll/about.html') 

def blog(request):
    return render(request, 'enroll/about.html')

def contact(request):
    return render(request, 'enroll/contact.html') 

def add_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data=adddata(request.POST)
            if data.is_valid(): 
                data.save()
                messages.success(request, 'Your POST add Successful !!!') 
                return HttpResponseRedirect('/dashboard/') 
        else:
            data=adddata()
        return render(request, 'enroll/adddata.html',{'datas':data})
    else:
        return HttpResponseRedirect('/login/') 

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            sm = User.objects.all() 
            user = request.user
            full_name = user.get_full_name() 
            gps = user.groups.all() 
            fm = Post.objects.all() 
            ip = request.session['ip'] 
            ct = cache.get('count', 0, version=user.pk) 
        else:
            sm = None 
            fm = Post.objects.all() 
            ip = request.session['ip']
            user = request.user
            full_name = user.get_full_name() 
            gps = user.groups.all() 
            ct = cache.get('count', 0, version=user.pk) 


        return render(request, 'enroll/dashboard.html',{'form':fm, 'full_name':full_name, 'gps':gps, 'sm': sm, 'ip':ip, 'ct': ct})   
    else:
        return HttpResponseRedirect('/login/') 

def SignUp(request):
    if request.method == "POST": 
        fm =signUp(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your Account create Successful !!!')
            user = fm.save() 
            group = Group.objects.get(name='author') 
            user.groups.add(group) 

    else:
        fm = signUp() 
    return render(request, 'enroll/signup.html', {'form':fm}) 

def log(request): 
    if not request.user.is_authenticated: 
        if request.method =='POST':
            form=loginForm(request=request, data=request.POST) 
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Your Account login Successful !!!') 
                    return HttpResponseRedirect('/dashboard/') 
        else:
            form = loginForm()        
        return render(request, 'enroll/login.html',{'form':form}) 
    else:
        return HttpResponseRedirect('/dashboard/')  

def logoutdata(request): 
    logout(request) 
    return HttpResponseRedirect('/') 

def update_data(request,id):
    if request.user.is_authenticated:
        if request.method == "POST": 
            sm = Post.objects.get(pk=id)
            fm =adddata(request.POST, instance=sm) 
            if fm.is_valid():
                messages.success(request, 'Your Account update Successful !!!') 
                fm.save()
                return HttpResponseRedirect('/dashboard/') 
        else:
            sm = Post.objects.get(pk=id)
            fm =adddata(instance=sm)
        return render(request, 'enroll/update.html',{'datas':fm}) 
    else:
        return HttpResponseRedirect('/login/') 

def delete_data(request, id):
    if request.user.is_authenticated:
        sm = Post.objects.get(pk=id)
        messages.error(request, 'Your Account delete Successful !!!') 
        sm.delete()
        return HttpResponseRedirect('/dashboard') 
    else:
        return HttpResponseRedirect('/login/')