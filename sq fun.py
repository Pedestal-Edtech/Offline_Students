a= int(input("a="))
b= int(input("b="))
c= input("enter your choice")
def master(c,a,b):
    def multi(a,b):
        print(a*b)
            
    def sqr(a,b):
        print(a**+b**+2*a*b)
    def cube(a,b):
        print(a**3+b**3+3*a**b+3*a*b**3)
    def pwr4(a,b):
        print(a**4+b**4-4*a**3*b+6*a**b**-4*a*b**3)  


    if c=="1":
        d = (multi(a,b)) 
    return d 
    
if c=="1":
   print(master(1,a,b))
   
