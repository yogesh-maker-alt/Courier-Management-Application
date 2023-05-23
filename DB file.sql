create database CUST_MANAGEMENT;
USE CUST_MANAGEMENT;
CREATE TABLE CUST_INFO
(CUST_ID INT PRIMARY KEY auto_increment  ,
CUST_NAME VARCHAR(60),
PH_NUMBER bigint (10) UNIQUE,
ADDRESS VARCHAR(60),
STATE varchar(30),
PINCODE INT 
);

CREATE TABLE CUST_ORDERS
(ORDER_ID INT PRIMARY KEY AUTO_INCREMENT,
PRODUCT_CATEGORY VARCHAR(70),
FROM_CITY VARCHAR(30),
TO_CITY VARCHAR(30),
ORDER_DATE DATE,
SHIPPED_DATE DATE, 
ORD_STATUS VARCHAR(50),
CUST_ID INT,
FOREIGN KEY (CUST_ID) REFERENCES CUST_INFO(CUST_ID)
);
use cust_management;
DESC CUST_INFO;

INSERT INTO CUST_INFO (`CUST_NAME`,`PH_NUMBER`,`ADDRESS`,`PINCODE`)
VALUES('SOHEM KULKARNI', 1234567880, 'KHARGHAR, MUMBAI',12345),
('RISHI CHAUDHARI',2136547890,'PRAKASH NAGAR,PUNE',78945);


create table Users
(
username varchar(30) unique not null primary key,
password varchar(20) unique not null,
name varchar(30) not null,
email varchar(30) unique not null
);

insert into users value ("yogesh7kolate","Yogesh@99","Yogesh","yogesh7kolate@gmail.com");
select * from users;
insert into users values("vrutik18","vrutik@123","Vrutik Parate");
insert into users values("CDACAdmin","CDAC@123","CDAC","yogesh11kolate@gmail.com");
