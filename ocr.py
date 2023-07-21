import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()
import streamlit as st
from PIL import Image
import cv2
import pytesseract


st.title("Optical Character Recognition.")

st.markdown("extracting text from image")

image = st.file_uploader("Upload your image over here", type=['png','jpg','jpeg'])


# def load_model():
#     reader = ocr.Reader(['en'],model_storage_directory='.')
#     return reader

# reader = load_model()

if image is not None:
    input_image = Image.open(image)
    st.image(input_image)
    
    with st.spinner("Runningg"):
        
        config = ('-l eng --oem 1 --psm 3')
        result = pytesseract.image_to_string(input_image)
        
        
        st.write(result)
        
    st.success("Done")
    st.balloons()
    
    
# else:
    
#     st.write("Upload an Image")
        
