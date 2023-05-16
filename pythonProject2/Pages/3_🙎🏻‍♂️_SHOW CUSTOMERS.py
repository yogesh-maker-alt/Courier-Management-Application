import streamlit as st
import mysql.connector
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid
from h import dbconnection

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image : url("https://assets-global.website-files.com/6009ec8cda7f305645c9d91b/6010843e4702bd1918217200_6002086f72b727e1b701d3df_blog-image.jpeg")
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()
mydb, mycursor = dbconnection()
st.header("Customer Details")
query=("select CUST_ID,CUST_NAME,PH_NUMBER,ADDRESS, STATE, PINCODE from CUST_INFO")
mycursor.execute(query)
df = pd.DataFrame(mycursor)
df = df.rename(columns={0: 'CUSTOMER ID', 1: 'CUSTOMER NAME', 2: 'MOBILE NUMBER', 3: 'ADDRESS', 4: 'STATE', 5: 'PINCODE'})

gb = GridOptionsBuilder.from_dataframe(df)

gridoptions = gb.build()

AgGrid(
    df,
    gridOptions=gridoptions
)