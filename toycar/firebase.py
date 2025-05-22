from pathlib import Path
import os
import json
import firebase_admin
import re
from firebase_admin import credentials, db
from dotenv import load_dotenv

# Load environment variables
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

# Preserve json_path for potential use elsewhere
current_directory = os.path.dirname(os.path.abspath(__file__))
FIREBASE_CRED_PATH = os.environ.get('FIREBASE_CRED_PATH')
json_path = os.path.join(current_directory, FIREBASE_CRED_PATH) if FIREBASE_CRED_PATH else None

def get_firebase_credentials():
    """Retrieve Firebase credentials from file path or environment variable."""
    if FIREBASE_CRED_PATH and os.path.exists(FIREBASE_CRED_PATH):
        return credentials.Certificate(FIREBASE_CRED_PATH)

    firebase_creds_str = os.environ.get("FIREBASE_CREDENTIALS_JSON")
    if firebase_creds_str:
        firebase_creds_dict = json.loads(firebase_creds_str)
        return credentials.Certificate(firebase_creds_dict)

    raise ValueError("Firebase credentials not found.")

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = get_firebase_credentials()
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://toycar-c1ce2-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# Global reference to the database
database_ref = db.reference()

def sanitize_email(email):
    return email.lower().replace("@", "<at>").replace(".", "<dot>")

def add_to_cart(email, item_id):
    item_ref = database_ref.child("users").child(email).child("items").child(item_id)
    if item_ref.get() is None:
        item_ref.update({"qty": 1})
    else:
        qty = item_ref.get("qty")
        qty = int(qty) if isinstance(qty, int) else 1
        item_ref.update({"qty": qty + 1})

def add_user(user, name, sanitized_email):
    users = database_ref.child("users")
    if users.child(sanitized_email).get() is not None:
        print(sanitized_email, "already exists")
        return
    users.child(sanitized_email).update({"items": []})
    print(f"User {sanitized_email} added")

def update_user_settings(sanitized_email, settings):
    print("Got here??")
    users = database_ref.child("users")
    users.child(sanitized_email).push({"settings": settings})

def get_cart(user):
    email = sanitize_email(user.email)
    user_data = database_ref.child("users").child(email).get()
    items = user_data.get("items") if user_data else None

    if not items:
        return None

    cart = {}
    for item_id, item_data in items.items():
        car_ref = database_ref.child(f"cars/{item_id}")
        name = car_ref.child("name").get()
        price = car_ref.child("price").get()
        cart[name] = price

    print(cart)
    return cart

def clear_cart(user):
    email = sanitize_email(user.email)
    database_ref.child("users").child(email).child("items").set({})

def delete_user_data(user):
    email = sanitize_email(user.email)
    database_ref.child("users").child(email).delete()

def save_contact_message(name, email, message):
    try:
        contact_ref = database_ref.child("contact_messages")
        contact_ref.update({
            "name": name,
            "email": email,
            "message": message
        })
        print("Contact message saved to Firebase.")
    except Exception as e:
        print(f"[Firebase Error] Failed to save contact message: {e}")