# gemini_id_detector.py
import google.generativeai as genai
import re
import os

# Get API Key securely
GEMINI_API_KEY = "AIzaSyAoqDMOEPH0I-Mre2h9xIAmTxs4bnmE5ug"
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Use correct model (Gemini Pro v1)
model = genai.GenerativeModel("gemini-pro")

PROMPT_TEMPLATE = """
You are an expert in ID redaction.
From the following OCR-extracted text, extract only valid ID numbers like Aadhaar, PAN, Passport, or Voter ID.
Respond strictly in this format:
[
  {"type": "Aadhaar", "value": "1234 5678 9012"},
  {"type": "PAN", "value": "ABCDE1234F"}
]

Text:
"""

def detect_ids_with_gemini(ocr_text):
    prompt = PROMPT_TEMPLATE + "\n" + ocr_text
    try:
        response = model.generate_content(prompt)
        print("[DEBUG] Gemini Response:", response.text)

        matches = re.findall(r'\{\s*"type":\s*"([^"]+)",\s*"value":\s*"([^"]+)"\s*\}', response.text)
        return [{"type": typ, "value": val} for typ, val in matches]
    except Exception as e:
        print(f"[ERROR] Gemini detection failed: {e}")
        return []
