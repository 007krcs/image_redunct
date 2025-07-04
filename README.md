# 📄 ID Masking Document Redactor (OCR + Gemini + FastAPI + Streamlit)

This tool allows you to upload identity documents (images or PDFs), detects personal ID information using OCR + Gemini AI, and generates a **new masked document** where only IDs are redacted with asterisks (e.g., passport number, Aadhaar, PAN, etc.).

---

## 🚀 Features

* OCR extraction from PDFs or images using EasyOCR
* Gemini Pro 1.5 model for AI-based ID detection
* Bounding box-based masking with layout preservation
* FastAPI backend to handle upload/download
* Streamlit frontend to preview redacted image before download
* Supports Indian, Korean, French, and global ID formats

---

## 📁 Folder Structure

```
.
├── main.py                    # Main masking pipeline (CLI)
├── api_app.py                # FastAPI backend
├── streamlit_ui.py           # Streamlit frontend
├── ocr_engine.py             # OCR logic (EasyOCR)
├── gemini_id_detector.py     # Gemini prompt & detection logic
├── mask_engine.py            # Masking logic with white box + asterisks
├── pdf_utils.py              # PDF to image + image to PDF tools
├── requirements.txt
├── uploads/                  # Uploaded files
├── output/                   # Redacted output files
└── temp_pages/               # Temporary PDF pages (if needed)
```

---

## 🧰 Installation

### 1. Clone the repo

```bash
git clone <your_repo_url>
cd image_red
```

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Gemini API Key

Create a `.env` file or pass directly in `gemini_id_detector.py`

```bash
export GEMINI_API_KEY=your-key-here      # macOS/Linux
set GEMINI_API_KEY=your-key-here         # Windows
```

Or edit `gemini_id_detector.py` to hardcode it:

```python
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "your-key"
```

---

## 🏃 How to Run

### Option 1: Local CLI (single file)

```bash
python main.py sample.jpg     # or sample.pdf
```

Masked file is saved in `output/` folder.

### Option 2: FastAPI + Streamlit (GUI Interface)

#### Start backend:

```bash
uvicorn api_app:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) to test upload API

#### Start frontend:

```bash
streamlit run streamlit_ui.py
```

Visit: [http://localhost:8501](http://localhost:8501) to use UI (upload & preview redacted image)

---

## 🧪 Supported Formats

* `.jpg`, `.jpeg`, `.png`, `.pdf`
* Passport numbers, Aadhaar, PAN, French ID, Korean ID, etc.

---

## 📦 Output

* Images: same format redacted and saved to `output/`
* PDFs: new masked PDF saved to `output/masked_output.pdf`

---

## ✅ To-Do (Optional Enhancements)

* Add ZIP output for multi-page PDFs
* Add watermark or signature
* Multilingual support with Langchain for ID extraction
* Role-based secure uploads

---

## 🧑‍💻 Contributors

* \[Your Name or Team]

---

## 📜 License

MIT or proprietary (update accordingly)
