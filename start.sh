#!/bin/bash

uvicorn api_app:app --host 0.0.0.0 --port 8000 &

streamlit run streamlit_ui.py --server.port=8501 --server.address=0.0.0.0
