def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c= a-b   
    print(c)
def multi(a,b):
    c=a*b 
    print(c)    
l=list(input("enter a list="))
op=input("enter a op=")
if op=="+":
    d=0
    for i in range(len(l)):
        d= d+float (l[i])
    print(d)
elif op=="*":
    d=1
    for i in range(len(l)):
     d= d*float(l[i])
    print(d)    
elif op=="/":
    d=1
    for i in range (len(l)):
        d=float(l[i])/d
    print(d) 
elif op=="-":
    d=int(l[0])
    for i in range(1,len(l)):
        d=d-int(l[i])
    print(d)
   