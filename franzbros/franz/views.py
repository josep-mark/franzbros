from django.shortcuts import render

def home(request):
    return render(request, "franz/home.html")

def services(request):
    return render(request, "franz/services.html")

def about(request):
    return render(request, "franz/about.html")

def contact(request):
    return render(request, "franz/contact.html")