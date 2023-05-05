import streamlit as st
from h import dbconnection
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid

################################### functions ##########################################

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color : #ADE4DB
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
def show_customers_by_id():
    # Create a cursor object
    Id = st.text_input("Enter Order ID", placeholder="Enter Order ID")
    submitted = st.button("🔍Search", key=1)

    if submitted:
        if Id.isdigit():
            mydb, mycursor = dbconnection()
            sql = "select * from cust_orders where order_id = %s"
            data = (Id,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if int(Id) in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'Order ID', 1: 'Product Category', 2: 'From City', 3: 'To City', 4: 'Order Date',
                                 5: 'Shipped Date', 6: 'Order Status', 7: 'Customer ID'})

                    gb = GridOptionsBuilder.from_dataframe(df)

                    gridoptions = gb.build()

                    AgGrid(
                        df,
                        gridOptions=gridoptions
                    )
                    rw = str(mycursor.rowcount) + " " + "record(s) fetched"
                    flag = False
                    break

            if flag:
                st.warning("Order Not Present")

            mycursor.close()
            mydb.close()

        elif Id.isalnum():
            st.error("Order ID should be digit only")
        elif Id == "":
            st.error("Order ID is empty")



##################################################################

def show_customers_by_product_category():
    # Create a cursor object
    product_Category = st.selectbox("Product Category",
                                    ["Select Product Category", "Electronics", "Textile", "Furniture", "Medical",
                                     "Others"])

    submitted = st.button("🔍Search", key=2)
    if submitted:
        if product_Category.isalpha():
            mydb, mycursor = dbconnection()
            sql = "select * from cust_orders where product_category = %s"
            data = (product_Category,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if product_Category in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'Order ID', 1: 'Product Category', 2: 'From City', 3: 'To City', 4: 'Order Date',
                                 5: 'Shipped Date', 6: 'Order Status', 7: 'Customer ID'})

                    gb = GridOptionsBuilder.from_dataframe(df)

                    gridoptions = gb.build()

                    AgGrid(
                        df,
                        gridOptions=gridoptions
                    )
                    rw = str(mycursor.rowcount) + " " + "Results"
                    st.success(rw)
                    flag = False
                    break

            if flag:
                st.warning("Order Not Present")

            mycursor.close()
            mydb.close()



##################################################################

def show_customers_by_from_city():
    # Create a cursor object
    from_city = st.text_input("Enter City", placeholder="City")

    submitted = st.button("🔍Search", key=3)
    if submitted:
        if from_city.isalpha():
            mydb, mycursor = dbconnection()
            sql = "select * from cust_orders where from_city = %s"
            data = (from_city,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if from_city in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'Order ID', 1: 'Product Category', 2: 'From City', 3: 'To City', 4: 'Order Date',
                                 5: 'Shipped Date', 6: 'Order Status', 7: 'Customer ID'})

                    gb = GridOptionsBuilder.from_dataframe(df)

                    gridoptions = gb.build()

                    AgGrid(
                        df,
                        gridOptions=gridoptions
                    )
                    rw = str(mycursor.rowcount) + " " + "Results"
                    st.success(rw)
                    flag = False
                    break

            if flag:
                st.warning("Order Not Present")

            mycursor.close()
            mydb.close()

        elif from_city.isdigit():
            st.error("City should not be number")
        elif from_city == "":
            st.error("From City is empty")

##################################################################

def show_customers_by_to_city():
    # Create a cursor object
    to_city = st.text_input("Enter City", placeholder="City",key='C')

    submitted = st.button("🔍Search", key=4)
    if submitted:
        if to_city.isalpha():
            mydb, mycursor = dbconnection()
            sql = "select * from cust_orders where to_city = %s"
            data = (to_city,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if to_city in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'Order ID', 1: 'Product Category', 2: 'From City', 3: 'To City', 4: 'Order Date',
                                 5: 'Shipped Date', 6: 'Order Status', 7: 'Customer ID'})

                    gb = GridOptionsBuilder.from_dataframe(df)

                    gridoptions = gb.build()

                    AgGrid(
                        df,
                        gridOptions=gridoptions
                    )
                    rw = str(mycursor.rowcount) + " " + "Results"
                    st.success(rw)
                    flag = False
                    break

            if flag:
                st.warning("Order Not Present")

            mycursor.close()
            mydb.close()

        elif to_city.isdigit():
            st.error("City should not be number")
        elif to_city == "":
            st.error("To City is empty")




##################################################################

def show_customers_by_orderdate():
    # Create a cursor object
    order_date = st.date_input("Enter Order Date")

    submitted = st.button("🔍Search", key=5)
    if submitted:
        mydb, mycursor = dbconnection()
        sql = "select * from cust_orders where order_date = %s"
        data = (order_date,)
        mycursor.execute(sql, data)
        myresult = mycursor.fetchall()
        flag = True
        for i in myresult:
            if order_date in i:
                df = pd.DataFrame(myresult)
                df = df.rename(
                    columns={0: 'Order ID', 1: 'Product Category', 2: 'From City', 3: 'To City', 4: 'Order Date',
                                 5: 'Shipped Date', 6: 'Order Status', 7: 'Customer ID'})

                gb = GridOptionsBuilder.from_dataframe(df)

                gridoptions = gb.build()

                AgGrid(
                    df,
                    gridOptions=gridoptions
                )
                rw = str(mycursor.rowcount) + " " + "Results"
                st.success(rw)
                flag = False
                break

        if flag:
          st.warning("Order Not Present")

        mycursor.close()
        mydb.close()

def show_customers_by_shipped_date():
    # Create a cursor object
    Shipped_date = st.date_input("Enter Shipped Date")

    submitted = st.button("🔍Search", key=6)
    if submitted:
            mydb, mycursor = dbconnection()
            sql = "select * from cust_orders where shipped_date = %s"
            data = (Shipped_date,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if Shipped_date in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'Order ID', 1: 'Product Category', 2: 'From City', 3: 'To City', 4: 'Order Date',
                                 5: 'Shipped Date', 6: 'Order Status', 7: 'Customer ID'})

                    gb = GridOptionsBuilder.from_dataframe(df)

                    gridoptions = gb.build()

                    AgGrid(
                        df,
                        gridOptions=gridoptions
                    )
                    rw = str(mycursor.rowcount) + " " + "Results"
                    st.success(rw)
                    flag = False
                    break

            if flag:
                st.warning("Order Not Present")

            mycursor.close()
            mydb.close()

def show_customers_by_order_status():
    # Create a cursor object
    order_status = st.selectbox("Order Status", ["Select Order Status", "In Transit", "Shipped", "Delivered", "Cancelled",
                                               "Out for Delivery"])
    submitted = st.button("🔍Search", key=7)
    flag = True
    if submitted:
        #if order_status.isalpha():
            mydb, mycursor = dbconnection()
            sql = "select * from cust_orders where ord_status = %s"
            data = (order_status,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            for i in myresult:
                if order_status in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'Order ID', 1: 'Product Category', 2: 'From City', 3: 'To City', 4: 'Order Date',
                                 5: 'Shipped Date', 6: 'Order Status', 7: 'Customer ID'})

                    gb = GridOptionsBuilder.from_dataframe(df)

                    gridoptions = gb.build()

                    AgGrid(
                        df,
                        gridOptions=gridoptions
                    )
                    rw = str(mycursor.rowcount) + " " + "Results"
                    st.success(rw)
                    flag = False
                    mycursor.close()
                    mydb.close()
                    break

    if submitted and flag:
        st.warning("Order Not Present")



def show_customers_by_cust_id():
    # Create a cursor object
    cust_id = st.text_input("Enter Customer ID", placeholder="Customer ID")

    submitted = st.button("🔍Search", key=8)
    if submitted:
        if cust_id.isdigit():
            mydb, mycursor = dbconnection()
            sql = "select * from cust_orders where cust_id = %s"
            data = (cust_id,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if int(cust_id) in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'Order ID', 1: 'Product Category', 2: 'From City', 3: 'To City', 4: 'Order Date',
                                 5: 'Shipped Date', 6: 'Order Status', 7: 'Customer ID'})

                    gb = GridOptionsBuilder.from_dataframe(df)

                    gridoptions = gb.build()

                    AgGrid(
                        df,
                        gridOptions=gridoptions
                    )
                    rw = str(mycursor.rowcount) + " " + "Results"
                    st.success(rw)
                    flag = False
                    break

            if flag:
                st.warning("Customer Not Present")

            mycursor.close()
            mydb.close()

        elif cust_id.isalpha():
            st.error("Customer Id should be number")
        elif cust_id == "":
            st.error("Customer ID is empty")

#############################################################
                    #Main Script
#add_bg_from_url()

tab1, tab2, tab3, tab4, tab5, tab6, tab7,tab8 = st.tabs([" Order ID  ", "Product Category", " Source City  ",
                                                    "  Destination City  ", "  Order Date  ", "Shipped Date","Order Status", "Customer ID"])

with tab1:
    st.header("Search by Order ID")
    show_customers_by_id()
with tab2:
    st.header("Search by Product Category")
    show_customers_by_product_category()

with tab3:
    st.header("Search by Source City")
    show_customers_by_from_city()
with tab4:
    st.header("Search by Destination City")
    show_customers_by_to_city()
with tab5:
    st.header("Search by Order Date")
    show_customers_by_orderdate()
with tab6:
    st.header("Search by Shipped Date")
    show_customers_by_shipped_date()
with tab7:
    st.header("Search by Order Status")
    show_customers_by_order_status()
with tab8:
    st.header("Search by Customer ID")
    show_customers_by_cust_id()



