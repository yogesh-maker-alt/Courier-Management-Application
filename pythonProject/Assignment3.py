
'''
sentence = input("Enter Sentence")
print(sentence.upper())
'''

# Write a program that reads in a list of names from a file and converts each name to uppercase before printing it out. The names in the file are separated by commas. For
# example, if the file contains "John, Mary, Susan", the program should print out "JOHN",
# "MARY", and "SUSAN"

'''
i=0
count = 0
print("Enter String")
str1 = input()
i=0
for i in range(len(str1)):
    if( (str1[i] == 'A') or (str1[i] == 'E') or (str1[i] == 'I') or (str1[i] == 'O') or (str1[i] == 'U' )) :
        if((str1[i-1] == " ") or (i==0)):
         count = count + 1
print(count)

'''

'''
Write a function that takes a string as input and returns a list of all the words in the string
that are longer than a specified length. The function should take two arguments: the string
and the minimum length of a word. For example, if the input string is "The quick brown
fox jumps over the lazy dog" and the minimum length is 4, the function should return
["quick", "brown", "jumps"].


def myFunction(names, length):
    names = names.split()
    str1 = ""
    for i in names:
        if((len(i)) > length):
             str1 = str1 + " " + i
    return str1

names = input("Enter String ")
length = int(input("Enter Length "))
st = myFunction(names,length)
print(st)

'''


import pandas as pd
df = pd.read_csv("C:\\Users\\ADMIN\\Downloads\\ADANIPORTS.csv")
print(df.to_string())
print("-------------------------------------------------------------------------------------------------------")
print(df.isnull().to_string())
print("-------------------------------------------------------------------------------------------------------")

new_df = df.dropna()
new_df.to_csv('n.csv')
