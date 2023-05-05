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

