import webbrowser

import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid
class Customers:
    def __init__(self):
        import mysql.connector
        self.mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
        self.mycursor = self.mydb.cursor()
    def show_customers(self):
        # Create a cursor object

        self.sql = "select * from cust_info"
        self.mycursor.execute(self.sql)

        self.myresult = self.mycursor.fetchall()

        # grid code to display customer data
        df = pd.DataFrame(self.mycursor)
        df = df.rename(columns={0: 'ID', 1: 'Name', 2: 'Address', 3: 'State', 4: 'Pincode', 5: 'Mobile Number'})
        gb = GridOptionsBuilder.from_dataframe(df)

        gridoptions = gb.build()

        AgGrid(
            df,
            gridOptions=gridoptions,
        )

        st.table(self.myresult)
        #st.table(self.myresult)
        rw = str(self.mycursor.rowcount) +" " + "record(s) fetched"
        st.success(rw)

        self.mycursor.close()
        self.mydb.close()

    def show_orders(self):
        # Create a cursor object

        self.sql = "select * from cust_orders"
        self.mycursor.execute(self.sql)

        self.myresult = self.mycursor.fetchall()

        st.table(self.myresult)
        #st.table(self.myresult)
        rw = str(self.mycursor.rowcount) +" " + "record(s) fetched"
        st.success(rw)

        self.mycursor.close()
        self.mydb.close()

    def show_customers_by_id(self, Id):
        # Create a cursor object
        sql = "select * from cust_info where cust_id = %s"
        data = (Id,)
        self.mycursor.execute(sql, data)
        self.myresult = self.mycursor.fetchall()

        for i in self.myresult:
            if int(Id) in i:
                st.table(self.myresult)
                rw = str(self.mycursor.rowcount) + " " + "record(s) fetched"
                st.success(rw)
                break
            elif not(int(Id) in i):
                st.warning("Customer Not Present")

        self.mycursor.close()
        self.mydb.close()


    def show_orders_by_id(self,id):
        self.id = id
        self.sql = "select * from cust_orders where order_id = %s"
        self.mycursor.execute(self.sql)

        self.myresult = self.mycursor.fetchall()

        st.table(self.myresult)
        #st.table(self.myresult)
        rw = str(self.mycursor.rowcount) +" " + "record(s) fetched"
        st.success(rw)

        self.mycursor.close()
        self.mydb.close()

# main script



option = st.sidebar.selectbox("Select an option", ("Select", "Customers", "Orders","Customer by ID","Order by ID"))
if option == "Customers":
    obj = Customers()
    obj.show_customers()
elif option == "Orders":
    obj = Customers()
    obj.show_orders()
elif option == "Customer by ID":
    ID = st.text_input("Enter Customer ID")
    if ID.isdigit():
        obj = Customers()
        obj.show_customers_by_id(ID)
    elif ID.isalnum():
        st.error("Customer ID should be digit only")
elif option == "Order by ID":
    ID = st.text_input("Enter Order ID")
    if ID.isdigit():
        obj = Customers()
        obj.show_customers_by_id(ID)
    else:
        st.error("Order ID should be digit only")
else:

    st.image("https://cdn.educba.com/academy/wp-content/uploads/2016/11/Customer-Data-1.png", width=800)










