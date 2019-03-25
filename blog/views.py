from django.shortcuts import render

# Create your views here.
def blog_home(request):
    return render(request, "home.html", {})


def blog_vale(request):
    return render(request, "vale.html", {})


def blog_ets(request):
    return render(request, "ets.html", {})


def blog_mmx(request):
    return render(request, "mmx.html", {})


def blog_transpanorama(request):
    return render(request, "transpanorama.html", {})