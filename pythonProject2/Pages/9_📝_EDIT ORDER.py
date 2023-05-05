import streamlit as st
from h import dbconnection
mydb, mycursor = dbconnection()

st.header("Edit Order Details")

tab1, tab2, tab3 =st.tabs([ "Product Category", "To City", "Order Status"])
with tab1 :
    ID = st.text_input("Enter Order ID", placeholder="Order ID", key=1)
    new = st.selectbox("New Product Category", ["Select Product Category", "Electronics", "Textile", "Furniture", "Medical", "Others"])
    flag = True
    if st.button("Update", key='b1'):
        if ID.isdigit():
            sql = "SELECT order_id FROM cust_orders"
            mycursor.execute(sql)
            rw = mycursor.rowcount
            result = mycursor.fetchall()
            for i in result:
                if int(ID) in i:
                    sql = "UPDATE cust_orders SET product_category = %s WHERE order_id = %s"
                    values = (new, int(ID))
                    mycursor.execute(sql, values)
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                    st.success("Product Category Updated Successfully")
                    flag = False
                    break

            if flag:
                st.error("Order Details Not Exist")
        elif ID == "" or new == "":
            st.error("All Fields are Mandatory")
        elif ID.isalnum() or new.isalnum():
            st.error("ID should be Digit and Name should not be digit")


with tab2 :
    ID = st.text_input("Enter Order ID", placeholder="Order ID", key=2)
    new = st.text_input("Enter To City", placeholder="To City")
    flag = True
    if st.button("Update", key='b2'):
        if ID.isdigit():
            sql = "SELECT order_id FROM cust_orders"
            mycursor.execute(sql)
            rw = mycursor.rowcount
            result = mycursor.fetchall()
            for i in result:
                if int(ID) in i:
                    sql = "UPDATE cust_orders SET to_city = %s WHERE order_id = %s"
                    values = (new, int(ID))
                    mycursor.execute(sql, values)
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                    st.success("To City / Destination City Updated Successfully")
                    flag = False
                    break

            if flag:
                st.error("Order Details Not Exist")
        elif ID == "" or new == "":
            st.error("All Fields are Mandatory")
        elif ID.isalnum() or new.isalnum():
            st.error("ID should be Digit and Name should not be digit")

with tab3:
        ID = st.text_input("Enter Order ID", placeholder="Order ID", key=3)
        new = st.selectbox("Order Status", ["Select Order Status", "In Transit", "Shipped", "Delivered", "Cancelled", "Out for Delivery"])

        Flag = True
        if st.button("Update", key='b3'):
            if ID.isdigit():
                sql = "SELECT order_id FROM cust_orders"
                mycursor.execute(sql)
                rw = mycursor.rowcount
                result = mycursor.fetchall()
                for i in result:
                    if int(ID) in i:
                        sql = "UPDATE cust_orders SET Ord_status = %s WHERE order_id = %s"
                        values = (new, int(ID))
                        mycursor.execute(sql, values)
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                        st.success("Order Status Updated Successfully")
                        Flag = False
                        break

                if Flag:
                    st.error("Order Details Not Exist")
            elif ID == "" or new == "":
                st.error("All Fields are Mandatory")
            elif ID.isalnum() or new.isalnum():
                st.error("ID should be Digit and Name should not be digit")