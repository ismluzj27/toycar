from pathlib import Path

import os
import json
import firebase_admin
import re
from firebase_admin import credentials, db
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

FIREBASE_CRED_PATH = os.environ.get('FIREBASE_CRED_PATH')

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory,
FIREBASE_CRED_PATH)
###
def get_firebase_credentials():
    # Try loading from file path (local dev)
    cred_path = os.environ.get("FIREBASE_CRED_PATH")
    if cred_path and os.path.exists(cred_path):
        return credentials.Certificate(cred_path)
    # Else, try from string (Vercel env var)
    firebase_creds_str = os.environ.get("FIREBASE_CREDENTIALS_JSON")
    if firebase_creds_str:
        firebase_creds_dict = json.loads(firebase_creds_str)
        return credentials.Certificate(firebase_creds_dict)
    raise ValueError("Firebase credentials not found.")
    # Initialize only if not already initialized
if not firebase_admin._apps:
    cred = get_firebase_credentials()
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://toycar-c1ce2-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
##


# cred = credentials.Certificate(json_path)
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://toycar-c1ce2-default-rtdb.asia-southeast1.firebasedatabase.app/'
# })

# Reference to the Realtime Database
database_ref = db.reference()

def add_to_cart(email, item_id):
    item_ref = database_ref.child("users").child(email).child("items").child(item_id)
    if item_ref.get() is None:
        item_ref.update({
            "qty": 1
        })
    else:
        quant = str(item_ref.get("qty"))
        qty = int(re.search(".*: ([0-9]+)", quant).group(1))
        print(qty)
        item_ref.update({
            "qty": qty + 1
        })

def add_user(user, name, email):
    users = database_ref.child("users")
    if users.child(email).get() is not None:
        print(email, "already exists")
        return
    users.child(email).update({
        "items": []
    })
    print(f"User {email} added")


def get_cart(user):
    email = sanitize_email(user.email)
    # ETag is enabled
    items = database_ref.child("users").child(email).get("items")[0]
    if not items:
        return None
    ilist = list(items.values())[0].keys()
    cart = {}
    for product_id in list(ilist):
        car_ref = database_ref.child(f"cars/{product_id}")
        name = car_ref.child("name").get()
        price = car_ref.child("price").get()
        cart[name] = price
    print(cart)
    return cart

def clear_cart(user):
    email = sanitize_email(user.email)
    items = database_ref.child("users").child(email).child("items")
    items.set({})

def delete_user_data(user):
    email = sanitize_email(user.email)
    database_ref.child("users").child(email).delete()

def sanitize_email(email):
    return email.lower().replace("@", "<at>").replace(".", "<dot>")