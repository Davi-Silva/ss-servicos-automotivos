from django.contrib import admin
from django.urls import path, include
from .views import homepage, consulting, about, contact
from blog import views as blog_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),  
    path('blog', include('blog.urls')),
    path('consultoria/', consulting, name="consulting"),
    path('sobre', about, name="about"),
    path('contato', contact, name="contact")

]
