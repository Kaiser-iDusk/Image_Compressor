import streamlit as st 
import numpy as np
from app_files.ai_ml import Compressor
# from PIL import Image
import cv2

cmp = Compressor()

st.title('Image Compressor')

st.subheader('Enter an image file to colour compress it: ')

file = st.file_uploader('Image Upload: ', ["png", "jpg", "jpeg"], accept_multiple_files=False)

if file is not None:
    try:
        img = cv2.imread(file)

    except Exception as e: 
        st.error(f"Error: {e}")