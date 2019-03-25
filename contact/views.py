from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse, JsonResponse
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("homepage")
        else: 
            print(contact_form.errors)
    else:
        contact_form = ContactForm()

    context= {
        "title" : "Contact",
        "form" : contact_form
    }


    return render(request, "contact.html", context)