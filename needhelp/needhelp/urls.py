"""needhelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.shortcuts import render, get_object_or_404, redirect
from . import views
from event import views as views_event

router = routers.DefaultRouter()
router.register(r'list', views_event.EventViewSet)


urlpatterns = [
    path('event/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('help/', include('help.urls')),
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include("django.contrib.auth.urls"), name="login"),
    path('accounts/profile/', views.profile, name="profile"),
    path('group/', include('group.urls')),

]
