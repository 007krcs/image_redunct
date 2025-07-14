#!/bin/bash

# Start FastAPI backend on port 8000 in background
uvicorn api_app:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend on port 10000 (publicly exposed)
streamlit run streamlit_ui.py --server.port 10000 --server.address 0.0.0.0
