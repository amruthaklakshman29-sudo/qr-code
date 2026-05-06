import streamlit as st
import qrcode
from PIL  import image

st.title("qrcode generator")
data=st.text_input("enter url")
if st.button("generate qr"):
  if data:
    qr=qrcode.make(data)
    qr.save("qr.png")

img= image.open("qr.png")
st.image(img, caption="generate qrcode")


with open("qr.png","rb") as f:
  st.download_button("download qr",f,file_name="qr.png")
else:
   st.warning("please enter some text")
