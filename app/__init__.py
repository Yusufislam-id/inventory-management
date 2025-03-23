from flask import Flask

# firebase
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Load Credentials
cred = credentials.Certificate(".\cred\cpsystem-adminsdk.json")
app_primary = firebase_admin.initialize_app(cred)

db = firestore.client()

# Import and register routes at the end to avoid circular imports
from app.routes import routes  
app.register_blueprint(routes)