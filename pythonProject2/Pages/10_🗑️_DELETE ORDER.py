import streamlit as st
from h import dbconnection

mydb, mycursor = dbconnection()
with st.form("deleteform"):
    count = 0
    st.header("Delete Orders")
    ID=st.text_input("Enter Order ID")
    if st.form_submit_button("Delete"):
        if ID.isdigit():
            sql = "SELECT order_id FROM cust_orders"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            for i in result:
                if int(ID) in i:
                    sql = "delete from cust_orders where order_id = %s"
                    values = (int(ID),)
                    mycursor.execute(sql, values)
                    rw = mycursor.rowcount
                    mydb.commit()

                    st.success(str(mycursor.rowcount) + " Order Deleted successfully")
                    break
                elif int(ID) not in i:
                    count += 1

            if rw == count:
                st.error("order Not Exist")

