##       Dictionary      ##

#   Dictionary holds the elements in key value pair
#   Where key are unique value
#   Dictionary are mutable type

#    Create Empty Dictionary
dit = {}
print(type(dit))
dit2 = dict()       # using Dict() method
print(type(dit2))

dit = {1: "One", 2: "Two", 3: "Three"}      # Key as integer
  #  Key: Value
print(dit)

dit2 = {'A':1, 'B':2, 'C':3}        # key as Alphabet
print(dit2)

print(dit.keys())

print(dit.values())

print(dit.items())

#   Dictionary with List, Tuple, Set == Mix Dictionary
dit3 = {1:5,3:[4,6],4:("Pune","Mumbai"), 5:{"Set1", 50, 10}}
print(dit3)

keys = {1,2,3,4}
values = {90,101,}  # values will be added to all keys
dit4 = dict.fromkeys(keys,values)
print(dit4)

'''values.append(12)
dit4 = dict.fromkey(keys,values)
print(dit4)'''

#print(dit1[1])

dit6 = {1:"Pune", 2:"mumbai", 3:"Nashik"}
print(dit6.get(3))

#       Update the value in Dictionary
dit5 = {'A':"One", 'B':"Two", "C":"Three"}
dit5['B'] = "one"
print(dit5)


name = input("Enter Your Name")
print("Helo " + name + "How are you?")


