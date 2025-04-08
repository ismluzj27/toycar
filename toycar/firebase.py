from pathlib import Path

import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

FIREBASE_CRED_PATH = os.environ.get('FIREBASE_CRED_PATH')

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory,
FIREBASE_CRED_PATH)

cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://toycar-c1ce2-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Reference to the Realtime Database
database_ref = db.reference()