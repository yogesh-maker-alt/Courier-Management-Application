# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
   # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    ## Conditional Statements If Else  ##
myFile = open("D:\Yogesh\Text.txt","r")
fileContent = myFile.readline()
print(fileContent.upper())
myFile.close()

n1 = int(input("Enter 1st Number"))
n2 = int(input("Enter 2nd Number"))

temp = n1
n1= n2
n2=temp

print(n1)
print(n2)

marks = 40
if marks > 16:
    print("Pass")
else:
    print("Fail")


str = "HELLO WoRLD"

if(str.isupper()):
    print(" String is Upper Case")
else:
    print("Lower Case")


number = int(input("Enter Number\n"))  # Taking input from User
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


if number > 0:
    print("Number is greater than 0")
else:
    print("Number is less than 0")



        ## Even ODD Number ##

str = "Bhusawal Nashik Jalgaon"

if(str[0]!=' '):
    print(str[0])
i=0
for i in  range(len(str)):
    if(str[i]==' '):
        print(str[i+1])





