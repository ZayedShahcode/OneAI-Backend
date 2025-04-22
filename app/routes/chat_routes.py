from flask import Blueprint, request, jsonify
import asyncio
from app.chatlogic.chatbot import chat
from app.utils.jwt_handler import token_required
from app.chatlogic.graph import bot

chat_bp = Blueprint('api', __name__)

@chat_bp.route('/',methods=['GET'])
@token_required
def home():
    return "Welcome to One AI"

@chat_bp.route('/chat',methods=['POST'])
@token_required
def chat_route():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400
    thread_id = request.user_id
    print(thread_id)
    message = data['message']
    response = asyncio.run(chat(thread_id,message))
    return jsonify({'response': response})