from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

# সব ধরনের অরিজিন থেকে রিকোয়েস্ট গ্রহণ করার জন্য CORS সেট করা হয়েছে
CORS(app, resources={r"/*": {"origins": "*"}}) 

# আপনার Groq API Key
API_KEY = "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"

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    # ব্রাউজার থেকে আসা প্রি-ফ্লাইট রিকোয়েস্ট হ্যান্ডেল করা
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        data = request.json
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Groq API-তে রিকোয়েস্ট পাঠানো হচ্ছে
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions", 
            json=data, 
            headers=headers
        )
        
        return jsonify(response.json())
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Render-এর পোর্ট অনুযায়ী সার্ভার চালু করা
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
