from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import blog_home, blog_ets, blog_mmx, blog_transpanorama, blog_vale

app_name="blog"
urlpatterns = [
    path('', blog_home, name="home"),
    path('vale', blog_vale, name="vale"),
    path('mmx', blog_mmx, name="mmx"),
    path('ets', blog_ets, name="ets"),
    path('transpanorama', blog_transpanorama, name="transpanorama")

]
