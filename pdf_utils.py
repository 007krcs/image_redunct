# pdf_utils.py
from pdf2image import convert_from_path
from PIL import Image
import os

TEMP_DIR = "temp_pages"
os.makedirs(TEMP_DIR, exist_ok=True)

def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path, dpi=300, output_folder=TEMP_DIR, fmt='jpeg')
    image_paths = []
    for i, img in enumerate(images):
        path = os.path.join(TEMP_DIR, f"page_{i+1}.jpg")
        img.save(path, "JPEG")
        image_paths.append(path)
    return image_paths

def save_images_to_pdf(image_paths, output_pdf_path):
    image_list = [Image.open(img_path).convert('RGB') for img_path in image_paths]
    if image_list:
        image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:])
