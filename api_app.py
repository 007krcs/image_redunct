from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil, os
import uuid
from main import process_document

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    ext = file.filename.split('.')[-1]
    input_path = os.path.join(UPLOAD_DIR, f"{file_id}.{ext}")

    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    output_path = process_document(input_path)

    if output_path and os.path.exists(output_path):
        filename = os.path.basename(output_path)
        return {"download_url": f"/download/{filename}"}
    return JSONResponse(status_code=500, content={"error": "Masking failed"})

@app.get("/download/{filename}")
def download_file(filename: str):
    filepath = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="application/octet-stream", filename=filename)
    return JSONResponse(status_code=404, content={"error": "File not found"})
