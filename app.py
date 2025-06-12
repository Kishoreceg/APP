import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to enhance the image using CLAHE (placeholder for your model)
def enhance_underwater_image(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    limg = cv2.merge((cl, a, b))
    enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return enhanced

st.set_page_config(page_title="Underwater Image Enhancement", layout="wide")
st.title("🌊 Underwater Image Enhancement")

st.markdown("""
Upload a blurred or poor-quality underwater image, and the app will apply image enhancement techniques to improve its clarity and visibility.
""")

# File uploader
uploaded_file = st.file_uploader("Upload Underwater Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and convert to OpenCV format
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Enhance image
    enhanced_image_bgr = enhance_underwater_image(image_bgr)
    enhanced_image_rgb = cv2.cvtColor(enhanced_image_bgr, cv2.COLOR_BGR2RGB)

    # Display images
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image, use_column_width=True)

    with col2:
        st.subheader("Enhanced Image")
        st.image(enhanced_image_rgb, use_column_width=True)
