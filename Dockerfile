# Use Python 3.13 base image
FROM python:3.13-slim

# Install system packages for OCR and scipy (gfortran, tesseract, poppler etc.)
RUN apt-get update && apt-get install -y \
    gfortran \
    tesseract-ocr \
    libgl1 \
    libglib2.0-0 \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose both ports for API (8000) and Streamlit (10000)
EXPOSE 8000
EXPOSE 10000

# Start both FastAPI and Streamlit using supervisord
CMD ["bash", "-c", "uvicorn api_app:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_ui.py --server.port 10000 --server.address 0.0.0.0"]
