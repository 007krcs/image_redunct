from pdf2image import convert_from_path
from PIL import Image
import os

def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    temp_dir = "temp_pages"
    os.makedirs(temp_dir, exist_ok=True)
    paths = []
    for i, img in enumerate(images):
        img_path = os.path.join(temp_dir, f"page_{i}.png")
        img.save(img_path, "PNG")
        paths.append(img_path)
    return paths

def save_images_to_pdf(image_paths, output_pdf_path):
    images = [Image.open(p).convert("RGB") for p in image_paths]
    if images:
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
