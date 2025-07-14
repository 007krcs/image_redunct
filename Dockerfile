FROM python:3.11-slim

# Install system dependencies for OCR, PDF, and SciPy
RUN apt-get update && apt-get install -y \
    gfortran \
    build-essential \
    cmake \
    pkg-config \
    libopenblas-dev \
    tesseract-ocr \
    poppler-utils \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000
EXPOSE 10000

# Start both FastAPI and Streamlit servers
CMD ["bash", "-c", "uvicorn api_app:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_ui.py --server.port 10000 --server.address 0.0.0.0"]
