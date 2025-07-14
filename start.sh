#!/bin/bash

# Start FastAPI backend in background
uvicorn api_app:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend (exposed port)
streamlit run streamlit_ui.py --server.port 10000 --server.address 0.0.0.0
