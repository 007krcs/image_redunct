import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="ID Masking Redactor", layout="centered")
st.title("🔒 ID Masking Document Redactor")
st.markdown("Upload your PDF or image file. The system will mask sensitive IDs using LLM logic.")

BACKEND_URL = "https://image-redunct.onrender.com"

uploaded_file = st.file_uploader("Choose a PDF or Image", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file:
    with st.spinner("Uploading and processing..."):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post(f"{BACKEND_URL}/upload/", files=files)

    if response.status_code == 200:
        download_info = response.json()
        download_url = f"{BACKEND_URL}{download_info['download_url']}"
        st.success("✅ Document processed and masked!")

        if uploaded_file.name.lower().endswith(("jpg", "jpeg", "png")):
            result_image = requests.get(download_url)
            if result_image.ok:
                st.image(Image.open(BytesIO(result_image.content)), caption="🔍 Masked Preview", use_column_width=True)

        st.markdown(f"[📥 Download Masked Document]({download_url})")
    else:
        st.error("❌ Something went wrong. Please try again.")
