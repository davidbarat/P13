from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='listgroup'),
    path('create/', views.create, name='creategroup'),

]