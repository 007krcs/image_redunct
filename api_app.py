from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil, os
import uuid
import subprocess
import glob

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run masking tool
    subprocess.run(["python", "main.py", file_path])

    # Detect output file
    if filename.lower().endswith(".pdf"):
        output_file = os.path.join("output", "masked_output.pdf")
    else:
        base_name = os.path.basename(file_path).split("_", 1)[-1]  # strip UUID
        matches = glob.glob(f"output/*{base_name}")
        output_file = matches[0] if matches else None

    if output_file and os.path.exists(output_file):
        return {"message": "File processed", "download_url": f"/download/{os.path.basename(output_file)}"}
    else:
        return {"message": "Masking failed. File not found."}

@app.get("/download/{filename}")
def download_file(filename: str):
    filepath = os.path.join("output", filename)
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="application/octet-stream", filename=filename)
    raise RuntimeError(f"File at path {filepath} does not exist.")