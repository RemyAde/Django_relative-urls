from django.urls import path
from appthree import views

app_name = 'appthree'

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name = 'relative') 
]