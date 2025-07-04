# mask_engine.py
from PIL import Image, ImageDraw, ImageFont
import re
import os

DEFAULT_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
if not os.path.exists(DEFAULT_FONT):
    DEFAULT_FONT = None

def mask_ids_on_document(image_path, ocr_result, id_entities):
    image = Image.open(image_path).convert("RGB")
    new_image = image.copy()
    draw = ImageDraw.Draw(new_image)

    id_values = [entity['value'] for entity in id_entities]

    for (bbox, text, conf) in ocr_result:
        for id_val in id_values:
            # Normalize and match IDs flexibly
            id_regex = re.escape(id_val).replace(r"\ ", r"\s*").replace("-", r"\s*")
            if re.search(id_regex, text.replace(" ", "").replace("-", ""), re.IGNORECASE):
                top_left = tuple(map(int, bbox[0]))
                bottom_right = tuple(map(int, bbox[2]))

                # Draw white box
                draw.rectangle([top_left, bottom_right], fill="white")

                # Draw masked text (asterisks)
                masked_text = "*" * len(text.strip())
                try:
                    font = ImageFont.truetype(DEFAULT_FONT, 14)
                except:
                    font = ImageFont.load_default()
                draw.text(top_left, masked_text, fill="black", font=font)
                break

    return new_image
