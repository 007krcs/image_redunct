# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all code
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose both backend and frontend ports
EXPOSE 8000
EXPOSE 10000

# Run the combined startup script
CMD ["./start.sh"]
