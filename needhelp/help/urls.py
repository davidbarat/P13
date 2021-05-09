from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout2, name='logout2'),
    path('update_event/', views.update_event, name='update_event'),
    path('contact/', views.contact, name='contact'),
]
