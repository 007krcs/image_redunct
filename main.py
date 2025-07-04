from ocr_engine import extract_text_from_file
from gemini_id_detector import detect_ids_with_gemini
from mask_engine import mask_ids_on_document
from pdf_utils import convert_pdf_to_images, save_images_to_pdf
import sys, os

INPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else "sample.pdf"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"[INFO] Processing file: {INPUT_FILE}")

# Step 1: Convert PDF to images if needed
image_files = convert_pdf_to_images(INPUT_FILE) if INPUT_FILE.endswith(".pdf") else [INPUT_FILE]

masked_images = []

for img_path in image_files:
    print(f"[INFO] OCR on image: {img_path}")
    ocr_text, raw_data = extract_text_from_file(img_path)

    print("[INFO] Sending OCR text to Gemini for ID detection...")
    id_entities = detect_ids_with_gemini(ocr_text)

    print(f"[DEBUG] Gemini Detected IDs: {id_entities}")
    print("[INFO] Masking detected IDs...")
    masked_img = mask_ids_on_document(img_path, raw_data, id_entities)
    out_img_path = os.path.join(OUTPUT_DIR, os.path.basename(img_path))
    masked_img.save(out_img_path)
    masked_images.append(out_img_path)

if INPUT_FILE.endswith(".pdf"):
    print("[INFO] Saving masked images back to PDF...")
    save_images_to_pdf(masked_images, os.path.join(OUTPUT_DIR, "masked_output.pdf"))
    print("[INFO] Masked PDF saved at output/masked_output.pdf")
else:
    print(f"[INFO] Masked image saved at: {masked_images[0]}")