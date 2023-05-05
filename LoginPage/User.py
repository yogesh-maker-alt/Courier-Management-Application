import streamlit as st
st.success("Log")

'''

class Customers:
    def __init__(self):
        import mysql.connector
        self.mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
        self.mycursor = self.mydb.cursor()
    def show_customer(self):
        # Create a cursor object

        self.sql = "select * from cust_info"
        self.mycursor.execute(self.sql)

        self.myresult = self.mycursor.fetchall()
        st.table(self.myresult)
        rw = str(self.mycursor.rowcount) +" " + "record(s) fetched"
        st.success(rw)

        self.mycursor.close()
        self.mydb.close()

'''
'''
    def update_customer(self):
        self.sql = "select * from cust_info where username = %s"
        self.data =
        self.mycursor.execute(self.sql,self.data)

        self.myresult = self.mycursor.fetchall()
        st.table(self.myresult)
        rw = str(self.mycursor.rowcount) + " " + "record(s) fetched"
        st.success(rw)

        self.mycursor.close()
        self.mydb.close()
# main script


#o bj = Customers()
# obj.show_customer()
'''







