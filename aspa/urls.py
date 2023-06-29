from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
urlpatterns = [
  path('auth/', include('rest_auth.urls')),
  path('all/', views.get, name='get'),
  path('create', views.create_user, name='create-user'),
]