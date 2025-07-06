# gemini_id_detector.py
import google.generativeai as genai
import re
import os

# Securely load your key
GEMINI_API_KEY = "Your Key"
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Use accessible model
model = genai.GenerativeModel("models/gemini-1.5-pro")

PROMPT_TEMPLATE = """
You are an expert in identifying personal ID information from OCR-extracted text.
Extract only valid ID numbers from global identity documents such as Aadhaar, PAN, Passport, French National ID, Korean Passport, etc.
Also include Document Numbers, Birth Dates, Reference Numbers if they seem like identifiers.

Return ONLY in this JSON format:
[
  {"type": "Document No", "value": "X4RTBPFW4"},
  {"type": "Date of Birth", "value": "13 07 1990"}
]

OCR Text:
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
