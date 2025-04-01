from django.shortcuts import render, redirect


# Create your views here.

def blank(request):
    return redirect("index")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# TODO: POST!!!
def checkout(request):
    return render(request, "checkout.html")

def shop(request):
    return render(request, "shop.html")

def settings(request):
    return render(request, "settings.html")

def speed(request):
    return render(request, "speed.html")

def offroad(request):
    return render(request, "offroad.html")

def classic(request):
    return render(request, "classic.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")

def care(request):
    return render(request, "care.html")

def item(request, item_id):
    item_name = "Toy Car" # TODO implement, probably with db?
    item_desc = "This will be fixed in the back end"
    return render(request, "shoptemplate.html",
                  {"item_id": item_id, "item_name": item_name, "item_desc": item_desc})
