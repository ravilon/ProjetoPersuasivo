from flask import Flask

# Import the blueprint from routes.py
from app.routes import bp as api_bp

def create_app():
    app = Flask(__name__)

    # Register the Blueprint
    app.register_blueprint(api_bp)

    return app
