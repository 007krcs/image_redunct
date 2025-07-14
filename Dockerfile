# Use slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose backend (8000) and frontend (10000) ports
EXPOSE 8000
EXPOSE 10000

# Start both apps using start.sh
CMD ["./start.sh"]
