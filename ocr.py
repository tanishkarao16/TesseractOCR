import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()
import streamlit as st
from PIL import Image


st.title("Optical Character Recognition.")

st.markdown("extracting text from image")

image = st.file_uploader("Upload your image over here", type=['png','jpg','jpeg'])

if image is not None:
    input_image = Image.open(image)
    st.image(input_image)
    
    with st.spinner("Runningg"):
        
        config = ('-l eng --oem 1 --psm 3')
        result = pytesseract.image_to_string(input_image)
        
        
        st.write(result)
        
    st.success("Done")
    st.balloons()
    
