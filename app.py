import streamlit as st 
import numpy as np
from app_files.ai_ml import Compress
from PIL import Image
import cv2

# cmp = Compress()

st.title('Image Compressor')

st.subheader('Enter an image file to colour compress it: ')

file = st.file_uploader('Image Upload: ', ["png", "jpg", "jpeg"], accept_multiple_files=False)

if file is not None:
    try:
        img = Image.open(file)
        work_img = np.array(img)
        HEIGHT, WIDTH = work_img.shape 
        COMPH, COMPW = int(512 * (HEIGHT / WIDTH)), 512

        scaled_img = cv2.resize(work_img, (COMPW, COMPH))

        st.image(scaled_img, caption='Original Image')

        cmp = Compress(scaled_img)

    except Exception as e: 
        st.error(f"Error: {e}")