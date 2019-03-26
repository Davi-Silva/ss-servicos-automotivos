from django.shortcuts import redirect, render
# from .forms import ContactForm
from contact.forms import ContactForm


def homepage(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("homepage")
        else: 
            print(contact_form.errors)
    else:
        contact_form = ContactForm()
    context = {
        "title" : "SS CONSULTORIA AUTOMOTIVA",
        "form" : contact_form
    }
    return render(request, "homepage.html", context)


def consulting(request):
    context = {
        "title" : "Consultoria"
    }
    return render(request, "consulting.html", context)

def about(request):
    context = {
        "title" : "SOBRE"
    }

    return render(request, "about.html", context)

