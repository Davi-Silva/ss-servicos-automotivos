from django.shortcuts import render

# Create your views here.
def quotes_home(request):
    context = {
        "title": "ORÇAMENTO"
    }
    return render(request, "quotes.html", context)