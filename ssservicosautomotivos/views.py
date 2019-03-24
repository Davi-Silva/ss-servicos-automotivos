from django.shortcuts import redirect, render
# from .forms import ContactForm


def homepage(request):
    context = {
        "title" : "SS Consultoria Automotiva"
    }

    return render(request, "homepage.html", context)


def consulting(request):
    context = {
        "title" : "Consultoria"
    }
    return render(request, "servicos.html", context)

def about(request):
    context = {
        "title" : "Consultoria"
    }

    return render(request, "about.html", context)

def contact(request):
    context= {
        "title" : "Contact"
    }
    return render(request, "contact.html", context)