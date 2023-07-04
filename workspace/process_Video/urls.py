from django.urls import path
from . import views
urlpatterns = [
    path('processImage', views.processImage , name='processImage')
]
