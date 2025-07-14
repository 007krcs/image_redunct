from PIL import Image, ImageDraw, ImageFont
import re
import os
import random
import string

DEFAULT_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
if not os.path.exists(DEFAULT_FONT):
    DEFAULT_FONT = None

def normalize_text(text):
    return re.sub(r"[\s\-]", "", text).lower()

def generate_fake_id(length=9):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def mask_ids_on_document(image_path, ocr_result, id_entities):
    image = Image.open(image_path).convert("RGB")
    new_image = image.copy()
    draw = ImageDraw.Draw(new_image)
    id_values = [normalize_text(entity['value']) for entity in id_entities]

    for (bbox, text, conf) in ocr_result:
        norm_text = normalize_text(text)
        for id_val in id_values:
            if id_val in norm_text and abs(len(id_val) - len(norm_text)) <= 2:
                top_left = tuple(map(int, bbox[0]))
                bottom_right = tuple(map(int, bbox[2]))
                draw.rectangle([top_left, bottom_right], fill="white")

                fake_id = generate_fake_id(len(text.strip()))
                try:
                    font = ImageFont.truetype(DEFAULT_FONT, 14)
                except:
                    font = ImageFont.load_default()

                draw.text(top_left, fake_id, fill="black", font=font)
                break

    return new_image
