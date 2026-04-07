from flask import Flask
from flask_cors import CORS

def create_app():
    # Create the Flask application
    app = Flask(__name__)
    
    # Allow cross-origin requests
    CORS(app)
    
    # Register our routes
    from app.routes import main
    app.register_blueprint(main)
    
    return app
