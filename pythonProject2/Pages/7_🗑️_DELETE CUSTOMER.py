import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
mycursor = mydb.cursor()

st.header("Customer Order Management System")

nav = st.sidebar.radio("Please Select..!!!", ["Select", "Customer", "Orders"])

if nav == "Customer":
    ID = st.text_input("Enter Customer ID")
    if ID.isdigit():
        sql = "SELECT cust_id FROM cust_info WHERE cust_id = (%s)"
        values = tuple(ID)
        mycursor.execute(sql, values)
        result = mycursor.fetchall()
        if len(result) == 1 and result[0][0] == int(ID):
            delet = "delete from cust_info where cust_id=(%s)"
            values = tuple(ID)
            mycursor.execute(delet, values)
            mydb.commit()
            st.success("Deletion completed successfully")
            mydb.close()
            mycursor.close()
elif nav == "Orders":
    ID = st.text_input("Enter Customer ID")
    if ID.isdigit():
        sql = "SELECT order_id FROM cust_orders WHERE order_id = (%s)"
        values = tuple(ID)
        mycursor.execute(sql, values)
        result = mycursor.fetchall()
        if len(result) == 1 and result[0][0] == int(ID):
            delet = "delete from cust_orders where order_id =(%s)"
            values = tuple(ID)
            mycursor.execute(delet, values)
            mydb.commit()
            st.success("Deletion completed successfully")
            mydb.close()
            mycursor.close()