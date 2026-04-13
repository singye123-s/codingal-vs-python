try:
    age = int(input("enter the age: "))
    if(age<10):
        raise ValueError
    else:
        print("the age is invalid")


except ValueError:
    print("The age is not valid")