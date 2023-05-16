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
             background-image : url("https://assets-global.website-files.com/6009ec8cda7f305645c9d91b/6010843e4702bd1918217200_6002086f72b727e1b701d3df_blog-image.jpeg")
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def show_customers_by_id():
    # Create a cursor object
    Id = st.text_input("Enter ID", placeholder="Enter ID")
    submitted = st.button("🔍Search", key=1)

    if submitted:
        if Id.isdigit():
            mydb, mycursor = dbconnection()
            sql = "select CUST_ID,CUST_NAME,PH_NUMBER,ADDRESS, STATE, PINCODE from cust_info where cust_id = %s"
            data = (Id,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if int(Id) in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'CUSTOMER ID', 1: 'CUSTOMER NAME', 2: 'MOBILE NUMBER', 3: 'ADDRESS', 4: 'STATE',
                                 5: 'PINCODE'})

                    gb = GridOptionsBuilder.from_dataframe(df)

                    gridoptions = gb.build()

                    AgGrid(
                        df,
                        gridOptions=gridoptions
                    )
                    rw = str(mycursor.rowcount) + " " + "Results"
                    st.subheader(rw)
                    flag = False
                    break

            if flag:
                st.warning("Customer Not Present")

            mycursor.close()
            mydb.close()

        elif Id.isalnum():
            st.error("Customer ID should be digit only")
        elif Id == "":
            st.error("ID is empty")



##################################################################

def show_customers_by_Name():
    # Create a cursor object
    Name = st.text_input("Enter Name", placeholder="Enter Name")

    submitted = st.button("🔍Search", key=2)
    if submitted:
        if Name.isalnum():
            st.error("Customer Name should not be number")
        elif Name == "":
            st.error("Name is empty")
        else:
            mydb, mycursor = dbconnection()
            sql = f"select cust_name from cust_info where cust_name = '{Name}'"
            #data = (Name,)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if Name in i:
                    sql = "select CUST_ID,CUST_NAME,PH_NUMBER,ADDRESS, STATE, PINCODE from cust_info where cust_name = %s"
                    data = (Name,)
                    mycursor.execute(sql, data)
                    #myresult = mycursor.fetchall()
                    df = pd.DataFrame(mycursor)
                    df = df.rename(
                        columns={0: 'CUSTOMER ID', 1: 'CUSTOMER NAME', 2: 'MOBILE NUMBER', 3: 'ADDRESS', 4: 'STATE',
                                 5: 'PINCODE'})

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



##################################################################

def show_customers_by_Mobile():
    # Create a cursor object
    Mobile = st.text_input("Enter Mobile Number", placeholder="Enter Mobile Number")

    submitted = st.button("🔍Search", key=3)
    if submitted:
        if Mobile.isdigit():
            mydb, mycursor = dbconnection()
            sql = "select CUST_ID,CUST_NAME,PH_NUMBER,ADDRESS, STATE, PINCODE from cust_info where ph_number = %s"
            data = (Mobile,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if int(Mobile) in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'CUSTOMER ID', 1: 'CUSTOMER NAME', 2: 'MOBILE NUMBER', 3: 'ADDRESS', 4: 'STATE',
                                 5: 'PINCODE'})

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

        elif Mobile.isalpha():
            st.error("Mobile Number should  be number")
        elif Mobile == "":
            st.error("Mobile Number is empty")

##################################################################

def show_customers_by_state():
    # Create a cursor object
    State = st.text_input("Enter State", placeholder="Enter State")

    submitted = st.button("🔍Search", key=4)
    if submitted:
        if State.isalpha():
            mydb, mycursor = dbconnection()
            sql = "select CUST_ID,CUST_NAME,PH_NUMBER,ADDRESS, STATE, PINCODE from cust_info where state = %s"
            data = (State,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if State in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'CUSTOMER ID', 1: 'CUSTOMER NAME', 2: 'MOBILE NUMBER', 3: 'ADDRESS', 4: 'STATE',
                                 5: 'PINCODE'})

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

        elif State.isalnum():
            st.error("State should not be number")
        elif State == "":
            st.error("State is empty")

##################################################################

def show_customers_by_pincode():
    # Create a cursor object
    Pincode = st.text_input("Enter Pincode", placeholder="Pincode")

    submitted = st.button("🔍Search", key=5)
    if submitted:
        if Pincode.isdigit():
            mydb, mycursor = dbconnection()
            sql = "select CUST_ID,CUST_NAME,PH_NUMBER,ADDRESS, STATE, PINCODE from cust_info where pincode = %s"
            data = (Pincode,)
            mycursor.execute(sql, data)
            myresult = mycursor.fetchall()
            flag = True
            for i in myresult:
                if int(Pincode) in i:
                    df = pd.DataFrame(myresult)
                    df = df.rename(
                        columns={0: 'CUSTOMER ID', 1: 'CUSTOMER NAME', 2: 'MOBILE NUMBER', 3: 'ADDRESS', 4: 'STATE',
                                 5: 'PINCODE'})

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

        elif Pincode.isalpha():
            st.error("Customer Name should be number")
        elif Pincode == "":
            st.error("Pincode is empty")


#############################################################
                    #Main Script





#add_bg_from_url()

css = '''
<style>
    .stTabs [data-baseweb="tab-highlight"] {
        background-color:black;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["ID", "Name", "Mobile Number", "State", "Pincode"])

with tab1:
  st.header("Search by ID")
  show_customers_by_id()
with tab2:
   st.header("Search by Name")
   show_customers_by_Name()

with tab3:
    st.header("Search by Mobile Number")
    show_customers_by_Mobile()
with tab4:
    st.header("Search by State")
    show_customers_by_state()
with tab5:
    st.header("Search by Pincode")
    show_customers_by_pincode()





