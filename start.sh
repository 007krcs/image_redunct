#!/bin/bash

# Start FastAPI in background
echo "Starting FastAPI..."
uvicorn api_app:app --host 0.0.0.0 --port 8000 &

# Start Streamlit (in foreground)
echo "Starting Streamlit..."
exec streamlit run streamlit_ui.py --server.port=8501 --server.address=0.0.0.0
