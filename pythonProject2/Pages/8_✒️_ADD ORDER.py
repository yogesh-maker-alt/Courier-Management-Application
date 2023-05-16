import streamlit as st
from h import dbconnection

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color : black
         }}
         .st.subheader {{
            color : blue
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def add_order(PRODUCT_CATEGORY, FROM_CITY, TO_CITY, ORDER_DATE, SHIPPED_DATE, ORD_STATUS, CUST_ID):
    count = 0

    mydb, mycursor = dbconnection()
    sql = "INSERT INTO CUST_ORDERS (PRODUCT_CATEGORY, FROM_CITY, TO_CITY,ORDER_DATE,SHIPPED_DATE,ORD_STATUS,CUST_ID) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (PRODUCT_CATEGORY, FROM_CITY, TO_CITY, ORDER_DATE, SHIPPED_DATE, ORD_STATUS, CUST_ID)
    #st.success(ORDER_DATE)
    mycursor.execute(sql, val)
    mydb.commit()
    #for i in myresult:
     #   if int(order_id) in i:
      #      st.warning("Order ID Already Exist")
       #     break
     #    if int(self.mobile_number) in i:
       #     st.warning("Mobile Number Already Exist")
      #      break
            # changes add in db
        #elif (int(self.cid) not in i) and (int(self.mobile_number) not in i):
         #   count += 1

    # for i in self.result:
    #t.success(myresult)
    if mycursor.rowcount > 0:
        st.success("Product Category : " + PRODUCT_CATEGORY + " | Order Date : " + str(ORDER_DATE) + " | Shipped Date : " +
                   " | Shipped Date : " + str(SHIPPED_DATE) + " | Order Status : " + ORD_STATUS + " | Customer ID : " + CUST_ID)
    rw = str(mycursor.rowcount) + " " + "Order Added Successfully"
    st.success(rw)

    mycursor.close()
    mydb.close()

# main script

add_bg_from_url()

with st.form("myform1"):
        st.subheader("Enter Orders Details")
        PRODUCT_CATEGORY = st.selectbox("Product Category", ["Select Product Category", "Electronics", "Textile", "Furniture", "Medical", "Others"])
        FROM_CITY = st.text_input("Enter From City:", placeholder="From City")
        TO_CITY = st.text_input("Enter To City: ", placeholder="To City")
        ORDER_DATE = st.date_input("Enter Ordered Date")
        SHIPPED_DATE = st.date_input("Enter Shipped Date")
        ORD_STATUS = st.selectbox("Order Status", ["Select Order Status", "In Transit", "Shipped", "Delivered", "Cancelled", "Out for Delivery"])
        CUST_ID = st.text_input("Enter Customer ID", placeholder="Customer ID")
        submitted = st.form_submit_button("Create")

        if submitted and (len(PRODUCT_CATEGORY) and (ORDER_DATE != "") and (SHIPPED_DATE != "") and len(ORD_STATUS)) != 0 :
            if CUST_ID.isdigit():
                st.success("DOne")
                add_order(PRODUCT_CATEGORY, FROM_CITY, TO_CITY, ORDER_DATE, SHIPPED_DATE, ORD_STATUS, CUST_ID)
            else:
                st.error("Order ID should be Digit")
        elif (submitted):
            st.error("All fields are mandatory")
