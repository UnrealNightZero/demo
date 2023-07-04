from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def shop(request):
    if request.method == "GET":
        return render(request,"shop.html")

def add(request):
    if request.method == "GET" and request.user.has_perm('is_superuser'):
        return render(request,"add.html")
    else:
        return HttpResponse("無權限訪問")