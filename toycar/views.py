import json

from django.shortcuts import render, redirect
from .firebase import database_ref, add_user, add_to_cart, sanitize_email, get_cart
from django.contrib.auth import logout

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect("index")

def blank(request):
    return redirect("index")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# TODO: POST!!!
def checkout(request):
    if not request.user.is_authenticated:
        return redirect("login")
    cart = get_cart(request.user)
    return render(request, "checkout.html",
                  {"cart_items": cart, "sum": sum (cart.values()) }) # TODO :make template show carts

def shop(request):
    return render(request, "shop.html",
                  {})

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
    if request.method == "POST":
        body = json.loads(request.body.decode('UTF-8'))
        id = body['id']
        email = None
        if request.user.is_authenticated:
            email = sanitize_email(request.user.email)
            add_to_cart(email, id)
        else:
            print("UNAUTH")
            return redirect("login") # TODO: how login??
        print(id)
        return redirect("shop")

    car_ref = database_ref.child(f"cars/{item_id}")
    if car_ref.get() is None:
        return redirect('shop')

    item_name = car_ref.child("name").get()
    item_desc = car_ref.child("desc").get()
    item_price = car_ref.child("price").get()
    item_category = ""
    match car_ref.child("category").get():
        case "speed":
            item_category = "Speed Cars"
        case "offroad":
            item_category = "Offroad Cars"
        case "classic":
            item_category = "Classic Cars"
    return render(request, "shoptemplate.html",
                  {"item_id": item_id, "item_name": item_name, "item_desc": item_desc,
                   "item_price": item_price, "item_category": item_category})


def auth_google_oauth2(request,state):
    print("request yo")
    user = request.user
    name = user.get_full_name()  # or user.first_name + user.last_name
    email = user.email  # usually mapped automatically
    add_user(user, name, email)
    return redirect('shop')
