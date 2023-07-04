from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages , auth
# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        username =  request.POST.get("username")
        password =  request.POST.get("password")
        check = User.objects.filter(username=username)
        if check:
            messages.error(request, 'Account already exists')
            return render(request,"register.html")
        else:
            User.objects.create_user(
                username=username,
                password=password
            )
            return redirect("/login")

def change(request):
    if request.method == "GET":
        return render(request,"change.html")
    else:
        username =  request.POST.get("username")
        password =  request.POST.get("password")
        check = User.objects.filter(username=username)
        if check:
            u = User.objects.get(username=username)
            u.set_password(password)
            u.save()
            return redirect("/")
        else:
            messages.error(request, 'check Account error')
            return render(request,"change.html")

def login(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "GET":
        return render(request,"login.html")
    else:
        username =  request.POST.get("username")
        password =  request.POST.get("password")
        user_obj =  auth.authenticate(username=username,password=password)
        if user_obj:
            auth.login(request,user_obj)
            return redirect("/")
        messages.error(request, 'username or password error')
        return render(request,"login.html")

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('/')