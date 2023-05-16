import streamlit as st

def dbconnection():
    import mysql.connector
    mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
    mycursor = mydb.cursor()
    return mydb, mycursor



