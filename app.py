import streamlit as st 
import numpy as np
from app_files.ai_ml import Compress
import cv2
import io
from PIL import Image
import os

# cmp = Compress()

st.title('Image Compressor')

st.subheader('Enter an image file to colour compress it: ')

file = st.file_uploader('Image Upload: ', ["png", "jpg", "jpeg"], accept_multiple_files=False)

if file is not None:
    try:
        img = Image.open(file)
        work_img = np.array(img)
        # print(work_img.shape)
        HEIGHT, WIDTH = work_img.shape[0], work_img.shape[1]
        COMPH, COMPW = int(256 * (HEIGHT / WIDTH)), 256

        scaled_img = cv2.resize(work_img, (COMPW, COMPH))

        st.image(scaled_img, caption='Original Image')

        cmp = Compress(scaled_img)

        val = st.slider("Select number of image clusters: ", 2, 64, 16, 1)

        output = cmp.get_output(int(val))

        st.image(output, caption='Compressed Image')

        btn = st.button("Apply Changes")

        if btn:
            dnld_img = cv2.resize(output, (WIDTH, HEIGHT))

            buffer = io.BytesIO()
            dnld_img = Image.fromarray(dnld_img)
            dnld_img.save(buffer, format="PNG")
            buffer.seek(0)

            st.download_button("Download", data=buffer, file_name="comp_out.png", mime="image/png") 

    except Exception as e: 
        st.error(f"Error: {e}")