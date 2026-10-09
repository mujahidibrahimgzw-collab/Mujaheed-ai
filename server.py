<html>
        <head><title>Downloaded HTML</title></head>
        <body>
            <pre style="white-space: pre-wrap; word-wrap: break-word;">from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# === SAKA API KEY DINKA ANAN - genai.configure(api_key="AQ.Ab8RN6La2XVC39f1D5XTQpoLAuRzYzdgoi2PNLK4wKCaYNLseQ")
model = genai.GenerativeModel('gemini-1.5-flash')

# === CODES NA SIRRI - KOWA BA ZAI GANI BA ===
# Idan mutum ya biya 8133661931, ka bashi daya daga nan a WhatsApp 08133661931
CODES_MASU_INGANCI = [
    "MUJ-8133-01",
    "MUJ-8133-02",
    "MUJ-8133-03",
    "MUJ-8133-04",
    "MUJ-8133-05",
    "MUJ-8133-06",
    "MUJ-8133-07",
    "MUJ-8133-08",
    "MUJ-8133-09",
    "MUJ-8133-10",
    "KANO-2024",
    "JAMB-AI-01"
]

@app.route('/verify', methods=['POST'])
def verify():
    code = request.json.get('code','').strip().upper()
    for valid in CODES_MASU_INGANCI:
        if code == valid.upper():
            return jsonify({"ok": True})
    return jsonify({"ok": False})

@app.route('/tambaya', methods=['POST'])
def tambaya():
    tambaya = request.json.get('tambaya','')
    prompt = f"Kai ne Mujaheed AI malami daga Kano, amsa da Hausa mai sauki: {tambaya}"
    amsa = model.generate_content(prompt)
    return jsonify({"amsa": amsa.text})

@app.route('/')
def gida():
    return "Mujaheed AI yana aiki!"

app.run(host='0.0.0.0', port=10000)</pre>
        </body>
    </html>