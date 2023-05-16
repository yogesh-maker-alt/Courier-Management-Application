import streamlit as st
import mysql.connector

class Customers:

    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
        self.mycursor = self.mydb.cursor()

    def add_customer(self,name,mobile_number,address,state,pincode):
        # Create a cursor object
        #self.cid = cid
        self.name = name
        self.pincode = pincode
        self.mobile_number = mobile_number
        self.address = address
        self.state = state

        sql = "select ph_number from cust_info"
        self.mycursor.execute(sql)
        self.result = self.mycursor.fetchall()
        count = 0
        for i in self.result:

            #if int(self.cid) in i:
             #   st.warning("Customer ID Already Exist")
              #  break
            if int(self.mobile_number) in i:
                st.warning("Mobile Number Already Exist")
                break
            elif int(self.mobile_number) not in i:
                count += 1
# changes add in db
        if count == self.mycursor.rowcount:
            column = "INSERT INTO CUST_INFO (cust_name,ph_number,address,state,pincode) VALUES (%s,%s,%s,%s,%s)"
            value = (self.name, self.mobile_number, self.state,self.address, self.pincode)
            self.mycursor.execute(column, value)
            self.mydb.commit()
            st.success(" Name : " + self.name + " | Mobile Number : " + self.mobile_number +
                           " | Address : " + self.address + " | State : " + self.state + " | Pincode : " + self.pincode)
            rw = str(self.mycursor.rowcount) + " " + "Customer Details Added Successfully"
            st.success(rw)

        self.mycursor.close()
        self.mydb.close()






###################################################################

# main script

st.subheader("CUSTOMER DETAILS ")
#st.tabs
with st.form("my_form1"):
        st.subheader("Enter Customers Details")
       # cid = st.text_input("Enter ID")
        name = st.text_input("Enter Name",placeholder="Name")
        mobile_number = st.text_input("Enter Mobile Number",placeholder="Mobile Number")
        address = st.text_input("Enter Address",placeholder="Address")
        state = st.text_input("Enter State",placeholder="State")
        pincode = st.text_input("Enter Pincode",placeholder="Pincode")
        submitted = st.form_submit_button("Create")
if submitted and len(name) and len(mobile_number) and len(address) and len(state) and len(pincode) != 0:

        if len(mobile_number) == 10:
            obj = Customers()
            obj.add_customer( name, mobile_number, address, state, pincode)
        else:
            st.error("Mobile Number Should be 10 Digit Only")
elif (submitted):
        st.error("All fields are mandatory")




