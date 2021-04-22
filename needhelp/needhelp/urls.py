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
    path('sms/', views.broadcast_sms, name='sms'),
]
