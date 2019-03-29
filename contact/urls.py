from django.contrib import admin
from django.urls import path, include
from blog import views as blog_view
from contact import views as contact_view

app_name="contact"
urlpatterns = [
    path('', contact_view.contact, name="home"),
    path('contato-enviado', contact_view.contact_success, name="sent")
]
