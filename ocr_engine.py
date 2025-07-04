# ocr_engine.py
import easyocr
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_file(image_path):
    result = reader.readtext(image_path)
    
    text_lines = []
    for (bbox, text, conf) in result:
        if conf > 0.4:
            text_lines.append(text)
    
    full_text = "\n".join(text_lines)
    return full_text, result  # returning both for visual masking
