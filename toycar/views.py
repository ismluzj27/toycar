from django.shortcuts import render, redirect


# Create your views here.

def blank(request):
    return redirect("index")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def shop(request):
    return render(request, "shop.html")
