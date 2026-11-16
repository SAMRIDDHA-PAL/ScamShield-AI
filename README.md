# 🛡️ ScamShield AI

ScamShield AI protects people from fraud calls. Paste any suspicious call transcript, and our AI tells you in seconds if it's a SCAM, SUSPICIOUS, or SAFE.

Built for Arthaton 2026 - Solo Project.

## Features
- Paste any call transcript in any language
- AI-powered detection with Risk Score (0-100)
- Explains WHY it's a scam and What To Do
- Works even if AI fails - has offline local check
- 2 Demo buttons to test instantly

## Tech Stack
Python, Flask, HTML, CSS, JavaScript, Google Gemini AI

AI Model: Google Gemini 2.0 Flash (via Gemini API) + Offline Rule-based Fallback

## How to Run
1. pip install -r requirements.txt
2. Create .env file with GEMINI_API_KEY=your_key
3. python app.py
4. Open http://127.0.0.1:5000
