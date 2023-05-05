
import streamlit as st
import webbrowser

with st.form("my_form1"):
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password")
    submitted = st.form_submit_button("Login")
    if submitted:
            webbrowser.open('http://localhost:8501/')

