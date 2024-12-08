import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Global variable for Firestore client
_db_client = None

def get_db():
    global _db_client
    if _db_client is None:
        # Path to your JSON key file

        json_key_path = 'C:/Users/ravil/OneDrive/Documentos/GitHub/iAthenAPI/iAthen/db-connection/firebase_credentials.json'

        # Initialize Firebase only once
        cred = credentials.Certificate(json_key_path)
        firebase_admin.initialize_app(cred)

        # Create Firestore client
        _db_client = firestore.client()

    return _db_client