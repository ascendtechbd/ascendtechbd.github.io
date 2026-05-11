from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

# এটি খুব জরুরি: যাতে আপনার ওয়েবসাইট থেকে রিকোয়েস্ট আসতে পারে
CORS(app, resources={r"/*": {"origins": "*"}})

# আপনার Groq API Key
API_KEY = "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"

# এই রুটটিই আপনার HTML খুঁজছে
@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat_handler():
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        user_data = request.json
        
        # Groq API এর জন্য হেডার
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Groq API-তে রিকোয়েস্ট পাঠানো
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json=user_data,
            headers=headers
        )
        
        return jsonify(response.json())

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# হোম পেজে জাস্ট চেক করার জন্য (ব্রাউজারে লিঙ্ক ওপেন করলে এটি দেখাবে)
@app.route('/')
def home():
    return "Ascend Tech BD AI Server is Running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
