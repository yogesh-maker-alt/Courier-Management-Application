import streamlit as st
from h import dbconnection

mydb, mycursor = dbconnection()
with st.form("deleteform"):
    count = 0
    st.header("Delete Customer Account")
    ID=st.text_input("Enter Customer ID")
    if st.form_submit_button("Delete"):
        if ID.isdigit():
            sql = "SELECT cust_id FROM cust_info"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            for i in result:
                if int(ID) in i:
                    sql = "delete from cust_orders where cust_id = %s"
                    values = (int(ID),)
                    mycursor.execute(sql, values)
                    mydb.commit()
                    sql = "delete from cust_info where cust_id = %s"
                    values = (int(ID),)
                    mycursor.execute(sql, values)
                    mydb.commit()
                    mydb.close()
                    mycursor.close()
                    st.success(str(mycursor.rowcount) + " Customer Deleted successfully")
                    break

                elif int(ID) not in i:
                    count += 1

            if mycursor.rowcount == count:
                st.error("Customer Not Exist")

