#module => folder => .py file
'''module '''
'''mylist1 = [1,2,3,4,5,6,7]
mylist2 =  [x for x in range(2,11) if x%2==0]
print(mylist2)

print(sum(mylist1))
mylist1.count()'''

'''
num = int(input("Enter Number : "))
rev = 0
num2 = 0
while(num):
    rev = num % 10
    num2 = num2 * 10 + rev
    num = num // 10

print(num2)'''

'''
n = int(input("Enter range : "))

for i in range (1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact * j
    print("Factorial of", i, "is", fact)
'''








'''a = "ekfjeopfkeof fjpoejfoef kfnefnepfjpf infpiabcdefghij klmnop qrstuv wxyz"
b = "abcdefghijklmnopqrstuvwxyz"
flag = True
for i in b:
  if i not in a:
    print("Not a Pangram")
    flag = False
    break
if flag:
  print("Pangram")

'''

'''st = "Hello Welcome how are you"
st = st.split()
print(len(st))'''


'''list = [1,2,3,5,6]
count = 0
for i in list:
    count +=1
for i in range(count-1,-1,-1):
    print(list[i]," ",end="")

print()
print(count)
'''

class studentData:
  def __init__(self):
   self.main_list = []
   self.sub_list = []
  def add_student(self,id,name,course):
    self.id = id;
    self.name = name
    self.course = course
    self.sub_list = [ self.id,self.name ]
    self.main_list.append(self.sub_list)
    print("Student", self.sub_list,"Added Successfully")
  def remove_student(self,id,name):
      self.id = id;
      self.name = name

      for i in self.main_list:
          if self.id in i or self.name in i:
              self.main_list.remove(i)
              print("Student Removed Successfully")

  def display_students(self):
      print("Students Data (Total Records",len(self.main_list),")")
      for i in self.main_list:
        for j in i:
            print(j," ",end="")
        print()

  def display_students_by_course(self,course):
            if



obj = studentData()
obj.add_student(1,"Charu")
obj.add_student(2,"Pranal")
obj.add_student(3,"Sandip")
obj.display_students()
obj.remove_student(3,"Sandip")
obj.display_students()