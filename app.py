import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Yuvraj's Mosaic Maker", layout="centered")

# --- UI Header ---
st.title("🖼️ Photo Mosaic Generator")
st.write("Turn your memories into a mosaic masterpiece!")

# --- Sidebar Money Section ---
st.sidebar.header("💰 Support the Creator")
st.sidebar.write("I'm a first-year B.Tech student building cool stuff!")
st.sidebar.write("If you like this, feel free to support:")
st.sidebar.info("UPI ID: yourname@okaxis") # Change this to your real UPI

# --- Step 1: Upload ---
uploaded_file = st.file_uploader("Upload the main photo you want to transform", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Target Image", use_container_width=True)
    
    # --- Step 2: Process ---
    if st.button("Generate Mosaic 🚀"):
        with st.spinner("Our AI is building your mosaic..."):
            # This is where the processing logic will eventually go
            st.success("Mosaic Created!")
            st.balloons()
            st.image(img) # For now, it shows the same image. We will add the math later!
