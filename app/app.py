import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask
from flask import send_from_directory

app = Flask(__name__)

# Initialize DB
cred = credentials.Certificate(".\cred\cpsystem-adminsdk.json")
app_primary = firebase_admin.initialize_app(cred)
db = firestore.client()