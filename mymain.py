import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide",page_title="Image Bg remover")

st.write("## Remove Background from your image ")
st.write(":cat: Try uploading image to view their backgrounds removed magically.Full Quality images.")

st.sidebar.write("## upload and download :gear:")

MAX_FILE_SIZE=20*1024*1024   #5Mb

#Download the fixed image
def convert_img(img):
    buf=BytesIO()
    img.save(buf,format="PNG")
    byte_im=buf.getvalue()
    return byte_im

col1,col2=st.columns(2) 

def fix_img(upload):
    image=Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed=remove(image)

    col2.write("Bgfree Image :camera:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download bgfree image",convert_img(fixed),"fixed.png","image.png")


my_upload=st.sidebar.file_uploader("Upload an image", type=["png","jpg","jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Upload file smaller than 20MB ")
    else:
        fix_img(upload=my_upload)