import streamlit as st

name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if (st.button('Submit')):
    result = name.title()
    st.success(result)

m = st.number_input("enter")

if (st.button('Submit')):
    result = m.title()
    st.success(result)