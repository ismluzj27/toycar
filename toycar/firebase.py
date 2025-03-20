import firebase_admin
from firebase_admin import credentials, db
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_directory,
'toycar-c1ce2-firebase-adminsdk-fbsvc-8ed3a0d9bc.json')