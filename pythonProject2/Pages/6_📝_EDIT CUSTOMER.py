import streamlit as st
from h import dbconnection
mydb, mycursor = dbconnection()

st.header("Edit Customers Details")


tab1, tab2, tab3, tab4 = st.tabs(["Update Customer Name",'Update Customer Address', "Update Customer Phone number", 'Update Customer Pin Code'])

with tab1:
    ID = st.text_input("Enter Customer ID", placeholder="Customer ID", key=1)
    new = st.text_input("Enter Name", placeholder="Name")
    count = 0
    if st.button("Update", key='b1'):
        if ID.isdigit() and new.isalpha():
            sql = "SELECT cust_id FROM cust_info"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            rw = mycursor.rowcount
            for i in result:
                if int(ID) in i:
                    sql = "UPDATE cust_info SET cust_name = %s WHERE cust_id = %s"
                    values = (new, int(ID))
                    mycursor.execute(sql, values)
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                    st.success("Name Updated Successfully")
                    break
                elif int(ID) not in i:
                    count += 1
            if rw == count:
                st.error("Customer Not Exist")
        elif ID == "" or new == "":
            st.error("All Fields are Mandatory")
        elif ID.isalnum() or new.isalnum():
            st.error("ID should be Digit and Name should not be digit")


with tab2:
    ID = st.text_input("Enter Customer ID", placeholder="Customer ID", key=2)
    new = st.text_input("Enter Address", placeholder="Address")
    count = 0
    if st.button("Update", key='b2'):
     if ID.isdigit() and new.isalpha():
        sql = "SELECT cust_id FROM cust_info"
        mycursor.execute(sql)
        rw = mycursor.rowcount
        result = mycursor.fetchall()

        for i in result:
            if int(ID) in i:
                    sql = "UPDATE cust_info SET address = %s WHERE cust_id = %s"
                    values = (new, int(ID))
                    mycursor.execute(sql, values)
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                    st.success("Address Updated Successfully")
                    break
            elif int(ID) not in i:
                count += 1
        if rw == count:
            st.error("Customer Not Exist")
     elif ID == "" or new == "":
         st.error("All Fields are Mandatory")
     elif ID.isalnum() or new.isdigit():
         st.error("Customer ID should be digit and Address Should not be digit ")


with tab3:
    ID = st.text_input("Enter Customer ID", placeholder="Customer ID", key=3)
    number = st.text_input("Enter Mobile number", placeholder="Mobile Number")
    if st.button("Update", key='b3'):
      if ID.isdigit() and len(number) == 10 and number.isdigit():
         sql = "SELECT cust_id,ph_number FROM cust_info"
         mycursor.execute(sql)
         rw = mycursor.rowcount
         result = mycursor.fetchall()
         for i in result:
             if int(ID) in i and int(number) not in i:
                 sql = "UPDATE cust_info SET ph_number = %s WHERE cust_id = %s"
                 values = (int(number), int(ID))
                 mycursor.execute(sql, values)
                 mydb.commit()
                 mycursor.close()
                 mydb.close()
                 st.success("Mobile Number Updated Successfully")
                 break
             elif int(ID) not in i:
                 count += 1
             elif int(number) in i:
                 st.error("Mobile Number Already Exist")

         if rw == count:
             st.error("Customer Not Exist")
      elif ID == "" or new == "":
        st.error("All Fields are Mandatory")
      elif ID.isalnum() or len(number) != 10:
          st.error("Mobile Number Should be 10 Digits")

with tab4:
    ID = st.text_input("Enter Customer ID", placeholder="Customer ID", key=4)
    pincode = st.text_input("Enter Pin Code", placeholder="Pin Code")
    if st.button("Update", key='b4'):
        if ID.isdigit() and pincode != "":
            sql = "SELECT cust_id FROM cust_info"
            mycursor.execute(sql)
            rw = mycursor.rowcount
            result = mycursor.fetchall()
            for i in result:
                if int(ID) in i:
                    sql = "UPDATE cust_info SET PinCode = %s WHERE cust_id = %s"
                    values = (pincode, int(ID))
                    mycursor.execute(sql, values)
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                    st.success("Pincode Updated Successfully")
                    break
                elif int(ID) not in i:
                    count += 1
            if rw == count:
                st.error("Customer Not Exist")
        elif ID == "" or pincode == "":
            st.error("All Fields are Mandatory")
        elif ID.isalnum() or pincode.isalnum():
            st.error("ID and Pincode should be Digit Only")