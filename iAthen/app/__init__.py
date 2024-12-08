from flask import Flask
from app import db
from flasgger import Swagger
from app.db import get_db
# Import the blueprint from routes.py
from app.routes import bp as api_bp

def create_app():
    app = Flask(__name__)

    # Register the Blueprint
    app.register_blueprint(api_bp)

    # Initialize Swagger
    Swagger(app)

    # Test DB
    db = get_db()
    # Fetch data from a Firestore collection
    collection_ref = db.collection("users")
    docs = collection_ref.stream()

    # Print retrieved data
    for doc in docs:
        print(f"Document ID: {doc.id}")
        print(f"Data: {doc.to_dict()}")

    return app
