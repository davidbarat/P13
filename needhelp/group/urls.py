from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='listgroup'),
    path('create/', views.create, name='creategroup'),
    path('update/', views.update_group, name='updategroup'),
]
