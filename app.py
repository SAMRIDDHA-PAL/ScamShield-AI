import os
import json
import re
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def local_check(text):
    t = text.lower()
    weights = {"otp": 50, "blocked": 30, "suspended": 30, "kyc": 30, "verify": 20, "prize": 40, "lottery": 40, "urgent": 20, "account will be closed": 30}
    score = 0
    reasons = []
    for w, points in weights.items():
        if w in t:
            score += points
            reasons.append(f"Contains suspicious keyword: '{w}'")
    if score >= 70:
        return {"result": "SCAM", "risk_score": 95, "reasons": reasons, "action": "Do not share OTP or pay. Block this number."}
    if score >= 30:
        return {"result": "SUSPICIOUS", "risk_score": score, "reasons": reasons, "action": "Do not share personal details. Verify from official number."}
    return {"result": "SAFE", "risk_score": 10, "reasons": ["No scam keywords found. Looks like a normal call."], "action": "No action needed, but stay alert."}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_text = request.json.get('text', '')
    MODELS = ['gemini-2.5-flash', 'gemini-2.5-flash-lite', 'gemini-3.8-flash']
    for model_name in MODELS:
        try:
            print(f"Trying model: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents=f"""You are a Cyber Security Expert. Read this call and answer in JSON only. Call: "{user_text}" Format: {{"result": "SCAM / SUSPICIOUS / SAFE", "risk_score": 0-100, "reasons": ["reason 1", "reason 2"], "action": "what to do in 1 line"}}"""
            )
            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            return jsonify(json.loads(clean_text))
        except Exception as e:
            print(f"{model_name} failed: {e}")
            continue
    print("All AI models failed, using local check")
    return jsonify(local_check(user_text))

if __name__ == '__main__':
    app.run(debug=True) 