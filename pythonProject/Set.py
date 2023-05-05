
#    Set is Collection of Elements in Unordered Form, Unindexed Form
#    Sets Does not Allow Duplicate Elements
#   Set is immutable / Unchangeble

#   When the set is empty, Set will be of dictionary type
myset = {}
print(type(myset))

#   When the set is initialized it is of Set type
myset = {1,2,3,4}
print(type(myset))

print(myset)

#   Declaring Set using empty set method  ## Use Set method to Create Empty Set ##
myset = set()
print(type(myset))

myset = {4,1,7,0,-1}
print(myset)

#   We cannot add list, Set ie. Nested Set in Set
#   We can tuple in Set
# myset ={"Pune", "Mumbai", 1.1, 2.1, (2,3), {4,5}}


myset ={"Pune", "Mumbai", 1.1, 2.1, (2,3)}

myset.add(6)
print(myset)

print(myset.update([40,30]))
print(myset)

#   remove checks the element and if element exist it delete the element and if not exist then gives the error
myset.remove(1.1)
print(myset)

#   discard checks the element and if element exist it delete the element and if not exist then does not gives error
myset.discard(1)
print(myset)

myset2 = myset
print(id(myset) + id(myset2))

myset2 = myset.copy()
print(id(myset) + id(myset2))


##       Set Operation       ##
#   union : unique element present in both set
s = {1,3,4,5,67,8}
s1 = {21,4,3,687,798}

print(s | s1)

s.union(s1)

s.union(s1,myset)

#   Intersection  = Common Elements in Both Sets

s = {1,2,3,4,5}
s1 = {4,5,6,7,8}
print(s & s1)

# Difference    = Elements of first set which are not present in second set
print(s-s1)     # Elements of s which are not present in s1
print(s1-s)     # Elements of s1 which are not present in s