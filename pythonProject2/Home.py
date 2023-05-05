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
             background-color : black
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


#add_bg_from_url()

st.title("Welcome to Tiltas Couriers!")
st.header("Your Trusted Partner in delivery")
gif_url = "https://cdn.dribbble.com/users/1352653/screenshots/7009470/food_delivery.gif"
st.image(gif_url, width=600)
