from django.shortcuts import render, redirect
from .forms import QuoteForm
from django.contrib import messages
from .models import Quote

# Create your views here.

def quotes_home(request):
    if request.method == "POST":
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            quote_form.save()
            messages.success(request, 'Form submission successful')
            return redirect("quotes:success")
        else: 
            print(quote_form.errors)
    else:
        quote_form = QuoteForm()

    context= {
        "title" : "ORÇAMENTO",
        "form" : quote_form,
        "message" : messages
    }
    return render(request, "quotes.html", context)


def quotes_successfully_sent(request):
    context = {
        "title": "ORÇAMENTO"
    }
    return render(request, "success.html", context)







