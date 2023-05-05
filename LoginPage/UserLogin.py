import  streamlit as st
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page


def dbconnection():
    import mysql.connector
    mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
    mycursor = mydb.cursor()
    return mydb, mycursor

def login():

    st.text_input("User Name:", key="user_name", placeholder="User Name")
    st.text_input("Password:", key="password", type="password", placeholder="Password")
    login_btn = st.button("Login")


    if login_btn:
        user_name = st.session_state.user_name
        password = st.session_state.password
        mydb, mycursor = dbconnection()
        query = (f"select * from users where UserName = '{user_name}' and Password = '{password}'")
        #password)
        mycursor.execute(query)
        data = mycursor.fetchall()
        if data:
            st.success("Logged In")
            st.success(data)
            if 'Logged_Username' not in st.session_state:
               st.session_state['Logged_Username'] = data[0][2]
               st.success(st.session_state.Logged_Username)
               st.session_state['User_Role'] = data[0][0]
               switch_page("Home")

        else:
            st.error("Incorrect User name or Password")


def add_customer():
    st.text_input("Name:", key="add_name")
    st.text_input("username:", key="add_user_name")
    st.text_input("Password:", key="add_password", type="password")
    st.text_input("Confirm Password:", key="add_confirm_password", type="password")
    st.text_input("Email ID:", key="add_email")
    add_btn = st.button("Create an Account")

    if add_btn:
        add_name = st.session_state.add_name
        add_user_name = st.session_state.add_user_name
        add_password = st.session_state.add_password
        add_confirm_password = st.session_state.add_confirm_password
        add_email = st.session_state.add_email;
        if add_password == add_confirm_password:

            mydb, mycursor = dbconnection()
            sql = f"Select * from users where username = '{add_user_name}'"
            mycursor.execute(sql)
            acc_data = mycursor.fetchall()

            if acc_data:
                st.error("User name already exist try another user name")
            else:
                sql = "INSERT INTO users(UserName,Password,Name,email)VALUES (%s, %s, %s, %s)"
                data1 = (str(add_user_name), str(add_password), str(add_name), str(add_email))
               # print(sql, data1)
                mycursor.execute(sql, data1)
                mydb.commit()
                mydb.close()
                mycursor.close()
                st.success(f"{add_user_name} Account Created Successfully! Please Login")
        else:
            st.error("Passwords do not match.")


def login_auth():
    gif_url = (
        "https://cdn.dribbble.com/users/725346/screenshots/6727425/mds-collivery-animated-gif-enormous-strides.gif")
    st.image(gif_url)
    if 'Logged_Username' not in st.session_state:
        st.subheader("Login")
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        with tab1:
            login()

        with tab2:
            add_customer()
    else:
        st.success("You already logged in")


if ('Logged_Username' in st.session_state) and ('User_Role' in st.session_state):
    col1, col2 = st.columns(2)
    with col1:
        st.write("Hello", st.session_state.Logged_Username, "(", st.session_state.User_Role, ")")
    with col2:
        logout = st.button("Logout")
        if logout:
            del st.session_state.Logged_Username
            del st.session_state.User_Role
            switch_page("UserLogin")
            st.success("Logged Out Successfully")


st.title("Welcome to Tiltas Couriers")
login_auth()


