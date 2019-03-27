from django.shortcuts import render


def blog_home(request):
    return render(request, "home.html", {})


def blog_companies_list(request):
    return render(request, "companies-list.html", {})


def blog_vale(request):
    context ={
        'title': 'Vale'
    }
    return render(request, "vale.html", context)


def blog_ets(request):
    context = {
        'title': 'ETS'
    }
    return render(request, "ets.html", context)


def blog_mmx(request):
    context = {
        'title': 'MMX'
    }
    return render(request, "mmx.html", context)


def blog_transpanorama(request):
    context = {
        'title': 'Transpanorama'
    }
    return render(request, "transpanorama.html", context)


def blog_abb(request):
    context = {
        'title': 'ABB'
    }
    return render(request, "abb.html", context)


def blog_manserv(request):
    context = {
        'title': 'Manserv'
    }
    return render(request, "manserv.html", context)


def blog_harsco(request):
    context = {
        'title': 'Harsco'
    }
    return render(request, "harsco.html", context)