from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import blog_home, blog_ets, blog_mmx, blog_transpanorama, blog_vale, blog_manserv, blog_companies_list, blog_harsco, blog_abb

app_name="blog"
urlpatterns = [
    path('', blog_home, name="home"),
    path('vale', blog_vale, name="vale"),
    path('mmx', blog_mmx, name="mmx"),
    path('ets', blog_ets, name="ets"),
    path('transpanorama', blog_transpanorama, name="transpanorama"),
    path('harsco', blog_harsco, name="harsco"),
    path('abb', blog_abb, name="abb"),
    path('manserv', blog_manserv, name="manserv"),
    path('lista-empresas', blog_companies_list, name="list"),


]
