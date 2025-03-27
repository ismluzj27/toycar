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

def item(request, item_id):
    item_name = "placeholder" # TODO implement, probably with db?
    item_desc = "foo bar baz or whatever they say"
    return render(request, "shoptemplate.html",
                  {"item_id": item_id, "item_name": item_name, "item_desc": item_desc})
