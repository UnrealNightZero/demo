from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register , name='register'),
    path('change/', views.change , name='change'),
    path('login/', views.login , name='login'),
    path("logout/", views.logout , name='logout')
]
