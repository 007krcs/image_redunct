from ocr_engine import extract_text_from_file
from vertex_ai_handler import detect_ids_with_gemini
from mask_engine import mask_ids_on_document
from pdf_utils import convert_pdf_to_images, save_images_to_pdf
import os

def process_document(input_file):
    OUTPUT_DIR = "output"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if input_file.endswith(".pdf"):
        image_files = convert_pdf_to_images(input_file)
    else:
        image_files = [input_file]

    masked_images = []
    for img_path in image_files:
        ocr_text, raw_data = extract_text_from_file(img_path)
        id_entities = detect_ids_with_gemini(ocr_text)
        masked_img = mask_ids_on_document(img_path, raw_data, id_entities)
        out_img_path = os.path.join(OUTPUT_DIR, f"masked_{os.path.basename(img_path)}")
        masked_img.save(out_img_path)
        masked_images.append(out_img_path)

    if input_file.endswith(".pdf"):
        output_pdf = os.path.join(OUTPUT_DIR, "masked_output.pdf")
        save_images_to_pdf(masked_images, output_pdf)
        return output_pdf
    else:
        return masked_images[0]
