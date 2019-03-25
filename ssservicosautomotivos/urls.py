from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import homepage, consulting, about
from blog import views as blog_view
from contact import views as contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),  
    path('blog/', include('blog.urls'), name="blog"),
    path('consultoria/', consulting, name="consulting"),
    path('sobre', about, name="about"),
    path('contato', contact_view.contact, name="contact")

]
