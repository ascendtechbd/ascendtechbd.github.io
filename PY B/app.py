from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app) # এটি আপনার ওয়েবসাইট থেকে ডেটা আসার অনুমতি দেবে

# Groq API Configuration
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
# আপনার API Key এখানে বসানো হলো
API_KEY = "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"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # আপনার সার্ভার Groq-কে রিকোয়েস্ট পাঠাবে
        response = requests.post(GROQ_API_URL, json=data, headers=headers)
        return jsonify(response.json())
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)