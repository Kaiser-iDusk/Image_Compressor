import streamlit as st 
import numpy as np
from app_files.ai_ml import Compress
# from PIL import Image
import cv2

# cmp = Compress()

st.title('Image Compressor')

st.subheader('Enter an image file to colour compress it: ')

file = st.file_uploader('Image Upload: ', ["png", "jpg", "jpeg"], accept_multiple_files=False)

if file is not None:
    try:
        img = cv2.imread(file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        HEIGHT, WIDTH = img.shape 
        COMPH, COMPW = int(512 * (HEIGHT / WIDTH)), 512

        scaled_img = cv2.resize(img, (COMPW, COMPH))

        st.image(scaled_img, caption='Original Image')

        cmp = Compress(scaled_img)

    except Exception as e: 
        st.error(f"Error: {e}")