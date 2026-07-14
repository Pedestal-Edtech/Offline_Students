# 1. implicit 

a= 10
b= 14
c= a+b
print("sum of a and b:", c)

#1.id 

id(a)
id(b)
id(c)

# 1. type

type(a)
type(b)
type(c)

# 2. inplicit

d= "hello"
e= "world"
f= d + e
print(f) 

# 2 id
id(d)
id(e)
id(f)

# 2. type

type(d)
type (e)
type(f)


# 1 & 2 explicit

value = int(input("the value is:"))
print(value)

course = input("course name:")
print(course)

# 1 & 2 input

name = input("name of intern:")
age = int(input("age of intern:"))
post = input("post of inter:")
print(name)
print(age) 
print(post)

project = input("create a project:")
languages = input("use language:")
print(project)
print(languages)
 
 
# 5 list

print(dir(list))

list1 = ["chitra sharma", 21 , "sikar"]

list1[0]
list1[1]
list1.index("sikar")

list2 = ["archana","deepika","chitra","madhuram"]
list2[0:]
list2[3]
list2[:4]
list2[0:4]
list2.pop(2)
print(list2)
list2.append("chitra")
print(list2)


list3 =[1,2,3,4,5,6,7,3,4,5,6,9,2,8]
list3[-7:]
list3[-8:]
list3[-8:-1]
list3[0]
list3.index(5)
list3.count(2)
list3.sort()
print(list3)
list3.reverse()
list3.extend([2,3,5,6])
print(list3)

list4 =[list1,list2,list3]
print(list1)
print(list2)
list4(list1)

list5 = ["prrakash","gomati","archana","deepika","chitra","madhuram"]
print(list1,list2,list3,list5 )
list5.count("chitra")

list1.clear()
print(list1)
len(list3)
list6 = [1,3,4,5,5,7,7,9,9,0,9,5,5,3]
list6 = list(input("create list :"))
# print(list6)
# type(list6)
# id(list6)

list6 = [1,3,4,5,5,7,7,9,9,0,9,5,5,3]
user_value = int(input("create list :"))
for i in range(len(list6)): 
    if list6[i]==user_value:
        print("match found") 
    else:
        print("match not found")


# tuple

print(dir(tuple))

tuple1 = (1,2,3,4,5,6,7,8,2,4,6,7,8,4,5,6)



tuple1[4]
tuple1[0:]
tuple1.index(8)
len(tuple1)
tuple1.count(8)


class student:
    print("my name is ")
    self.name = name
    
class add:
    def g():
        a = 15
        b = 16
        c = 10 + 20
        return c
    obj = add
    obj.g()
