FROM python:3.11-slim

# Set environment variable to avoid interactive tzdata setup
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install system-level dependencies required for Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000
EXPOSE 10000

# Make sure start.sh is executable
RUN chmod +x ./start.sh

# Start both backend and frontend
CMD ["./start.sh"]
