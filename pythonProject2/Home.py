import streamlit as st
from PIL import Image
import mysql.connector


st.set_page_config(
    page_title="Tiltas Systems",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://png.pngtree.com/background/20210711/original/pngtree-corporate-website-design-flat-background-banner-picture-image_1106665.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.title("Welcome to Tiltas Systems!")
st.header("Your Trusted Partner in delivery")
st.image("https://5.imimg.com/data5/SELLER/Default/2020/12/EL/UC/FS/34223366/107-500x500.jpg", width=800)


