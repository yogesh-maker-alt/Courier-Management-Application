import streamlit as st
from h import dbconnection

def show_customers_by_id(Id):
    # Create a cursor object
    mydb, mycursor = dbconnection()
    sql = "select * from cust_info where cust_id = %s"
    data = (Id,)
    mycursor.execute(sql, data)
    myresult = mycursor.fetchall()
    flag = True
    for i in myresult:
        if int(Id) in i:
            st.table(myresult)
            rw = str(mycursor.rowcount) + " " + "record(s) fetched"
            st.success(i)
            flag = False
            break

    if flag:
        st.warning("Customer Not Present")


    mycursor.close()
    mydb.close()


#############################################################
#main script
Id = st.text_input("Enter ID",placeholder="Enter ID")

#if Id:
   # ID = st.text_input("Enter Customer ID")
submitted = st.button("🔍Search")
if submitted:
    if Id.isdigit():
        show_customers_by_id(Id)
    elif Id.isalnum():
        st.error("Customer ID should be digit only")
    elif Id == "":
        st.error("ID is empty")

