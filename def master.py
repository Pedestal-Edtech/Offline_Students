a= float(input("a="))
b= float(input("b="))
c= input("enter your choice=")
def master():
    def a1():
        print(a+b)
    def a2():
        print(a**2+b**2+2*a*b)
    def a3():
        print(a**3+b**3+3*a**2*b+3*a*b**2)
    def a4():
        print(a**4+b**4+4*a**3*b+6*a**2*b**2+4*a*b**3) 
    if c=="1":
        a1()
    elif c=="2":
        a2()
    elif c=="3":
        a3()
    elif c=="4":
        a4()                    
    else:
        print("enter a valid choice")  
master()
    


