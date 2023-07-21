import streamlit as st
from PIL import Image
import pytesseract
import shutil

st.title("Optical Character Recognition.")
st.markdown("extracting text from image")

# Find the path to the Tesseract executable dynamically
tesseract_cmd = shutil.which('tesseract')
if tesseract_cmd is None:
    st.error("Tesseract not found. Please ensure it is installed and accessible.")
    st.stop()

image = st.file_uploader("Upload your image over here", type=['png', 'jpg', 'jpeg'])

if image is not None:
    input_image = Image.open(image)
    st.image(input_image)

    with st.spinner("Running"):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        
        # Perform OCR using pytesseract
        result = pytesseract.image_to_string(input_image)

        st.write(result)

    st.success("Done")
    st.balloons()
