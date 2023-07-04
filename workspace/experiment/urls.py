from django.urls import path
from . import views
urlpatterns = [
    path('auto_data/', views.auto_data , name='auto_data'),
    path('exper/', views.exper , name='exper'),
    path('search/', views.search ,name='search'),
    path("search_2/",views.search_2,name='search_2'),
    path("search_3/",views.search_3,name='search_3'),
    path("api/data/",views.data,name='data')
]
