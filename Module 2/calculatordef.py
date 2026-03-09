choice = int(input("what would you like to calculate which numbers 1. for addition 2 for subtraction 3. for multiplication 4. for division"))
a = int(input("enter number."))
b = int(input("enter next number."))

def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

if choice==1:
    print(a,"+",b,"=",addition(a,b))
elif choice==2:
    print(a,"-",b,"=",substraction(a,b))
elif choice==3:
    print(a,"x",b,"=",multiplication(a,b))
elif choice==4:
    print(a,"/",b,"=",division(a,b))
else:
    print("invalid choice!")

