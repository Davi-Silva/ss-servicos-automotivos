from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import quotes_home

app_name="quotes"
urlpatterns = [
    path('', quotes_home, name="home"),
]
