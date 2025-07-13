# Use official Python 3.13 base image
FROM python:3.13-slim

# Install system dependencies needed for OCR, SciPy, and image processing
RUN apt-get update && apt-get install -y \
    gfortran \
    build-essential \
    tesseract-ocr \
    poppler-utils \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Upgrade pip and install all Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose both ports: 8000 (FastAPI) and 10000 (Streamlit)
EXPOSE 8000
EXPOSE 10000

# Run both FastAPI and Streamlit together
CMD ["bash", "-c", "uvicorn api_app:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_ui.py --server.port 10000 --server.address 0.0.0.0"]
