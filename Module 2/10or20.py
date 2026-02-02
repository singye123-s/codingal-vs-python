age = int(input("Enter age: "))

start = 10
end = 20

if age >= start:
    if age <= end:
        print("Age is between 10 and 20")
    else:
        print("Age is greater than 20")
else:
    print("Age is less than 10")
