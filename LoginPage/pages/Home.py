import pandas as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid
from streamlit_extras.switch_page_button import switch_page
import UserLogin


def dbconnection():
    import mysql.connector
    mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
    mycursor = mydb.cursor()
    return mydb, mycursor

def logout():
    if ('Logged_Username' in st.session_state) and ('User_Role' in st.session_state):
        col1, col2 = st.columns(2)
        with col1:
            msg = st.session_state.Logged_Username + " (" + st.session_state.User_Role + ")"
            st.success(msg)
        with col2:
            logout = st.button("Logout")
        if logout:
                del st.session_state.Logged_Username
                del st.session_state.User_Role
                switch_page("UserLogin")
                st.success("Logged Out Successfully")
        gif_url = "https://cdn.dribbble.com/users/1797873/screenshots/5310497/media/11f62c6a80a286dc84191b60bd0fb9d1.gif"
        st.image(gif_url, width=700)


def userView():
    mydb, mycursor = dbconnection()
    query = f"Select * from cust_info where cust_name = '{st.session_state.Logged_Username}'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    #st.table(myresult)
    id = 0
    name = ""
    number = 0
    address = ""
    state = ""
    pincode = ""
    flag = 1
    for i in myresult:
        id = i[0]
        name = i[1]
        number = i[2]
        address = i[3]
        state = i[4]
        pincode = i[5]
        flag = 2
        # animation

    tab1, tab2, tab3, tab4 = st.tabs(["Profile","Add Order","My Orders", "Log Out" ])
    with tab1:
            with st.form("form1"):
                if flag == 2:
                   newname = st.text_input("Name", value=name)
                   newnumber = st.text_input("Mobile Number", value=number)
                   newaddress = st.text_input("Address", value=address)
                   newstate = st.text_input("State", value=state)
                   newpincode = st.text_input("Pincode", value=pincode)
                   sub = st.form_submit_button("Update")
                   if sub:
                    sqlname = "UPDATE cust_info SET cust_name = %s WHERE cust_id = %s"
                    valuesname = (newname,id)
                    mycursor.execute(sqlname, valuesname)
                    mydb.commit()
                    sqlnumber = "UPDATE cust_info SET ph_number = %s WHERE ph_number = %s"
                    valuesnumber = (newnumber, number)
                    mycursor.execute(sqlnumber, valuesnumber)
                    mydb.commit()
                    sql = "UPDATE cust_info SET address = %s, state = %s, pincode = %s WHERE cust_id = %s"
                    values = (newaddress, newstate, newpincode, id)
                    mycursor.execute(sql, values)
                    mydb.commit()
                    st.success("Details Updated Successfully")
                elif flag == 1:
                     newname = st.text_input("Name", value=name)
                     newnumber = st.text_input("Mobile Number", value=number)
                     newaddress = st.text_input("Address", value=address)
                     newstate = st.text_input("State", value=state)
                     newpincode = st.text_input("Pincode", value=pincode)
                     sub = st.form_submit_button("Submit")
                     if sub:
                      sqlname = "insert into cust_info(cust_name,ph_number,address, state, pincode) values (%s,%s,%s,%s,%s)"
                      values = (newname, newnumber, newaddress, newstate, newpincode)
                      mycursor.execute(sqlname, values)
                      mydb.commit()

                      st.success("Details Updated Successfully")

    with tab2:
            with st.form("myform1"):
                st.subheader("Enter Orders Details")
                PRODUCT_CATEGORY = st.selectbox("Product Category",
                                            ["Select Product Category", "Electronics", "Textile", "Furniture",
                                             "Medical", "Others"])
                FROM_CITY = st.text_input("Enter From City:", placeholder="From City")
                TO_CITY = st.text_input("Enter To City: ", placeholder="To City")
                ORDER_DATE = st.date_input("Enter Ordered Date")
                submitted = st.form_submit_button("Submit")

                if submitted and (len(PRODUCT_CATEGORY) and (ORDER_DATE != "")):
                        sql = "INSERT INTO CUST_ORDERS (PRODUCT_CATEGORY, FROM_CITY, TO_CITY,ORDER_DATE,CUST_ID) VALUES (%s,%s,%s,%s,%s)"
                        val = (PRODUCT_CATEGORY, FROM_CITY, TO_CITY, ORDER_DATE, id)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Order Details Submitted Successfully")
                elif (submitted):
                    st.error("All fields are mandatory")
                else:
                    st.error("Order ID should be Digit")

    with tab3 :
        st.subheader("My Orders")
        sql = f"select cust_name, ph_number, order_id,product_Category, from_city, to_city, order_date,ord_status from cust_info ci, cust_orders co where ci.cust_id = '{id}' and co.cust_id = '{id}'"
        #values = (tuple(id), tuple(id))
        mycursor.execute(sql)
        flag = True
        rw = str(mycursor.rowcount) + " " + "Results"
        for i in myresult:
                df = pd.DataFrame(mycursor)
                df = df.rename(
                    columns={0:'CUSTOMER NAME', 1: 'MOBILE NUMBER', 2: "Order ID", 3: 'Product Category', 4: "From City",
                             5: "To City", 6: "Order Date", 7: "Order Status"})

                gb = GridOptionsBuilder.from_dataframe(df)

                gridoptions = gb.build()

                AgGrid(
                    df,
                    gridOptions=gridoptions
                )
                st.subheader(rw)
                flag = False
                break

        if flag:
            st.warning("You Have Not Placed Any Order Request")
    with tab4:
        logout()


        #animation + code


    mydb.close()
    mycursor.close()

# main/*

if 'Logged_Username' not in st.session_state:
    switch_page("UserLogin")
else:
    userView()
