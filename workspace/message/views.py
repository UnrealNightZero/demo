from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Message

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

def subit(request):
    if request.method == 'POST':
        author = request.user
        content = request.POST.get('content')
        message = Message(author=author, content=content)
        message.save()
        messages = Message.objects.all()
        return render(request, 'message_list.html',{'messages': messages})

def update(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        new_content = request.POST.get('new_content')

        message = Message.objects.get(id=message_id)
        message.content = new_content
        message.save()

        messages = Message.objects.all()
        return render(request, 'message_list.html', {'messages': messages})

def delete_message(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')

        message = Message.objects.get(id=message_id)
        message.content = "訊息已被 " + message.author + " 已收回"
        message.change = 0
        message.save()

        response = {'author': message.author}  # 將 author 包含在回應中
        return JsonResponse(response)