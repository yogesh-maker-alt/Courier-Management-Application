import streamlit as st

import mysql.connector
mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
mycursor = mydb.cursor()
def set_ph():
    CONTACT = st.text_input("Enter new phone number", "enter the number")
    if CONTACT.isdigit():
        sql = "UPDATE cust_info SET PH_NUMBER = (%s) WHERE cust_id = (%s)"
        values = (CONTACT, ID)
        mycursor.execute(sql, values)
        mydb.commit()
        st.write("phone number updated successfully")
    else:
        st.write("enter proper contact")


def set_add():
    new_address = st.text_input("Enter new address", "enter address")
    sql = "UPDATE cust_info SET address = (%s) WHERE cust_id = (%s)"
    values = (new_address, ID)
    mycursor.execute(sql, values)
    mydb.commit()


def set_pin():
    CONTACT = st.text_input("Enter new pincode number", "enter the number")
    if CONTACT.isdigit():
        sql = "UPDATE cust_info SET PINCODE = (%s) WHERE cust_id = (%s)"
        values = (CONTACT, ID)
        mycursor.execute(sql, values)
        mydb.commit()
        st.write("Pincode number updated successfully")
    else:
        st.write("enter proper pin")


st.header("Customer Order Management System")

nav = st.sidebar.radio("Please Select..!!!", ["Select", "Customer", "Orders"])

if nav == "Customer":
    select = st.selectbox("Customer: ", ['Select Customer Info', "Update Customer Info"])
    if select == "Update Customer Info":
        check = st.selectbox("select option: ",
                             ['Select','Update Customer Address', "Update Customer Phone number", 'Update Customer Pin Code'])

        if check == 'Update Customer Address':
            ID = st.text_input("Enter Customer ID", "enter id")
            if ID.isdigit():
                sql = "SELECT cust_id FROM cust_info WHERE cust_id = (%s)"
                values = (ID,)
                mycursor.execute(sql, values)
                result = mycursor.fetchall()

                if len(result) == 1 and result[0][0] == int(ID):
                    set_add()
                    st.write("Address updated successfully")
                else:
                    st.write("ID does not exist")

        if check == "Update Customer Phone number":
            ID = st.text_input("Enter Customer ID", "enter id")
            if ID.isdigit():
                sql = "SELECT cust_id FROM cust_info WHERE cust_id = (%s)"
                values = (ID,)
                mycursor.execute(sql, values)
                result = mycursor.fetchall()

                if len(result) == 1 and result[0][0] == int(ID):
                    set_ph()
                else:
                    st.write("ID does not exist")

        if check == 'Update Customer Pin Code':
            ID = st.text_input("Enter Customer ID", "enter id")
            if ID.isdigit():
                sql = "SELECT cust_id FROM cust_info WHERE cust_id = (%s)"
                values = (ID,)
                mycursor.execute(sql, values)
                result = mycursor.fetchall()
                if len(result) == 1 and result[0][0] == int(ID):
                    set_pin()
elif nav == "Orders":
    up_selection = st.selectbox("Update Order Details", ["Select", "Product Category", "Order Status"])

    if up_selection == "Product Category":

        up_id = st.text_input('Enter your order ID')
        p_category = st.text_input("Enter Product Category")
        if st.button("Submit"):  # check if id exist
            query = ("UPDATE cust_orders SET  product= %s WHERE order_id = %s")
            value = (p_category, up_id)
            mycursor.execute(query, value)
            mydb.commit()
            rw = mycursor.rowcount
            msg = st.success(str(rw) + " Updated Successfully")  # not showing properly check it
            mycursor.close()
            mydb.close()
    elif up_selection == "Order Status":
        up_id = st.text_input('Enter customer order ID')
        # p_status = st.text_input("Enter order status")
        p_status = st.selectbox("customer status", ['select', "Shipped", "Delivered", "cancelled"])
        if st.button("Submit"):
            query = ("UPDATE cust_orders SET ord_status = %s WHERE order_id = %s")
            value = (p_status, up_id)
            mycursor.execute(query, value)
            mydb.commit()
            rw = mycursor.rowcount
            msg = st.success(str(rw) + ' customer order are ' + p_status)
            mycursor.close()
            mydb.close()

