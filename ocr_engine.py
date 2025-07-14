import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_file(image_path):
    result = reader.readtext(image_path)
    text_lines = [text for (_, text, conf) in result if conf > 0.4]
    return "\n".join(text_lines), result
