from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.message_list, name='message_list'),
    path('subit/', views.subit, name = 'subit'),
    path('update_message/' ,views.update , name='update'),
    path('delete_message/' ,views.delete_message , name="delete_message")
]