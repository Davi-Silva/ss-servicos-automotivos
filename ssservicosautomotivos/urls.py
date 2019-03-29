from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import homepage, consulting, about
from blog import views as blog_view
from contact import views as contact_view
from quotes import views as quotes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),  
    path('blog/', include('blog.urls', namespace="blog"), name="blog"),
    path('orcamento/', include('quotes.urls', namespace="quotes"), name="quotes"),
    path('consultoria', consulting, name="consulting"),
    path('sobre', about, name="about"),
    path('contato/', include('contact.urls', namespace="contact"), name="contact")
]
