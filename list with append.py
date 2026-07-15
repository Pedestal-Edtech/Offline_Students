l1=list(input("L1="  ))
l2=[]
print(l1)
a=(input("enter a value to find="))
for i in range (len(l1)):
    if l1[i]==a:
     l2.append(i)
if len(l2) !=0:
    print(l2)
else:
    print("character not found")