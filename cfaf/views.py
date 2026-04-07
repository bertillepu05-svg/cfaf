from django.shortcuts import render


def index (request):
    return render(request, "pages/index.html")

def a_propos (request):
    return render(request, "pages/a-propos.html")

def contact (request):
    return render(request, "pages/contact.html")

def formations (request):
    return render(request, "pages/formations.html")

def evenements (request):
    return render(request, "pages/evenements.html")




