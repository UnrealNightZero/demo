from django.shortcuts import render
from django.http import HttpResponse
from member.models import USER
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.user.has_perm('is_superuser'):
        data_list = User.objects.all().filter(is_superuser=0)
        print (data_list)
        return render(request,"index.html",{"data_list":data_list})
    return render(request,"index.html",{"display":"none"})
def delete(request):
    if request.user.has_perm('is_superuser'):
        data_list = User.objects.all().filter(is_superuser=0)
        data_list.delete()
    return redirect("/")
