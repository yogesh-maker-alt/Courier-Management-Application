import webbrowser
import streamlit as st
import mysql.connector


mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
mycursor = mydb.cursor()

with st.form("my_form1"):
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password")
    submitted = st.form_submit_button("Login")
    if submitted:


        mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
        mycursor = mydb.cursor()
        sql = "select username, password from users"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.close()
        mycursor.close()
        for i in myresult:
            if ("Admin" in i) and ("12345" in i):
                webbrowser.open('http://localhost:8502/Home/')
                st.success("Login Successful")
            elif username == "" and password == "":
                st.warning("Enter Username and Password")
            elif (username not in i) or (password not in i):
                st.warning("Account Does Not Exist")

