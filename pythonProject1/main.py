# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user= 'root',
    password = "12345",
    port = "3306",
    database = "sys"
)

mycursor = mydb.cursor()
id = int(input("Enter ID : "))
name = input("Enter Name : ")
city = input("Enter City : ")

sql = (
    "insert into Employee(id,name,city)" 
    "values(%s,%s,%s)"
)
val = (id,name,city)
mycursor.execute(sql,val)
mydb.commit()

mycursor.execute('select * from Employee')
data = mycursor.fetchall()
for i in data:
    print(i)

