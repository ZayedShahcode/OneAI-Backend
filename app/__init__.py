import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.routes.chat_routes import chat_bp
from app.routes.auth_routes import auth_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app,
         resources={r"/*": {
             "origins": ["https://one-ai-phi.vercel.app"],
             "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
             "allow_headers": ["Content-Type", "Authorization"],
         }},
         supports_credentials=True)
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(chat_bp, url_prefix='/api')
   
    

    return app
