FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt . 
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1-mesa-glx \
    poppler-utils \
    fonts-dejavu-core \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Make start.sh executable
RUN chmod +x start.sh

# Expose both ports (FastAPI:8000, Streamlit:8501)
EXPOSE 8000 8501

# Default command
CMD ["./start.sh"]
