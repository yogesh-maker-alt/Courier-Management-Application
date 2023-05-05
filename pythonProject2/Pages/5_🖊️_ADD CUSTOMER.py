import streamlit as st
import mysql.connector


class Customers:

    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
        self.mycursor = self.mydb.cursor()

    def add_customer(self,cid,name,mobile_number,address,state,pincode):
        # Create a cursor object
        self.cid = cid
        self.name = name
        self.pincode = pincode
        self.mobile_number = mobile_number
        self.address = address
        self.state = state

        sql = "select cust_id, ph_number from cust_info"
        self.mycursor.execute(sql)
        self.result = self.mycursor.fetchall()
        count = 0
        for i in self.result:

            if int(self.cid) in i:
                st.warning("Customer ID Already Exist")
                break
            elif int(self.mobile_number) in i:
                st.warning("Mobile Number Already Exist")
                break
            elif (int(self.cid) not in i) and (int(self.mobile_number) not in i):
                count += 1
# changes add in db
        if self.mycursor.rowcount == count:
            column = "INSERT INTO CUST_ORDERS (PRODUCT,ORDER_DATE,SHIPPED_DATE,ORD_STATUS,CUST_ID) VALUES (%s,%s,%s,%s,%s)"
            value = (self.PRODUCT, self.ORDER_DATE, self.SHIPPED_DATE, self.order_status, self.CUST_ID)
            self.mycursor.execute(column, value)
            self.mydb.commit()
            self.result = self.mycursor.fetchone()
            for i in self.result:
                st.success(i)
        rw = str(self.mycursor.rowcount) + " " + "record(s) affected"
        st.success(rw)

        self.mycursor.close()
        self.mydb.close()




    def add_order(self,PRODUCT,ORDER_DATE,SHIPPED_DATE,ORD_STATUS,CUST_ID):
        # Create a cursor object
        self.PRODUCT = PRODUCT
        self.ORDER_DATE = ORDER_DATE
        self.pincode = SHIPPED_DATE
        self.order_status = ORD_STATUS
        self.CUST_ID = CUST_ID

        count = 0
        sql = "select order_id from cust_orders"
        self.mycursor.execute(sql)
        self.result = self.mycursor.fetchall()

        for i in self.result:
            if int(self.order_id) in i:
                st.warning("Order ID Already Exist")
                break
            elif int(self.mobile_number) in i:
                st.warning("Mobile Number Already Exist")
                break
                # changes add in db
            elif (int(self.cid) not in i) and (int(self.mobile_number) not in i):
                count +=1

        #for i in self.result:
        st.success(self.result)
        rw = str(self.mycursor.rowcount) + " " + "record(s) affected"
        st.success(rw)

        self.mycursor.close()
        self.mydb.close()

###################################################################

# main script


option = st.sidebar.selectbox("Select an option", ("Select", "Customers", "Orders"))
# Perform selected CRUD Operations
if option == "Customers":
    st.subheader("CUSTOMER ORDER MANAGEMENT SYSTEM ")
    #st.tabs
    with st.form("my_form1"):
        st.subheader("Enter Customers Details")
        cid = st.text_input("Enter ID")
        name = st.text_input("Enter Name")
        mobile_number = st.text_input("Enter Mobile Number")
        address = st.text_input("Enter Address")
        state = st.text_input("Enter State")
        pincode = st.text_input("Enter Pincode")
        submitted = st.form_submit_button("Create")
    if submitted and len(cid) and len(name) and len(mobile_number) and len(address) and len(state) and len(pincode) != 0:
        obj = Customers()
        obj.add_customer(cid, name, mobile_number, address, state, pincode)
    elif (submitted):
        st.error("All fields are mandatory")


elif option == "Orders":
    with st.form("myform1"):
        st.subheader("Enter Orders Details")
        PRODUCT = st.text_input("Enter Product Name : ")
        ORDER_DATE = st.date_input("Enter Ordered Date :")
        SHIPPED_DATE = st.date_input("Enter Shipped Date")
        ORD_STATUS = st.text_input("Enter Order Status : ")
        CUST_ID = st.text_input("Enter customer ID: ")
        submitted = st.form_submit_button("Create")

        if submitted and (len(PRODUCT) and (ORDER_DATE != "")  and (SHIPPED_DATE != "") and len(ORD_STATUS)) != 0 :
            if CUST_ID.isdigit():
                obj = Customers()
                obj.add_order(PRODUCT, ORDER_DATE, SHIPPED_DATE, ORD_STATUS, CUST_ID)
            else:
                st.error("Customer ID should be Digit Only")
        elif (submitted):
            st.error("All fields are mandatory")
        else:
            st.image("https://www.mmppicture.co.in/wp-content/uploads/2020/08/CB-Background-27-857x1080.jpg")

