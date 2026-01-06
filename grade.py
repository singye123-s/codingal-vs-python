eng = float(input("enter your english grades: "))
math = float(input("enter your math grades: "))
sci = float(input("enter your science grades: "))
gym = float(input("enter your gym grades: "))
his= float(input("enter your history grades: "))

avg = (eng+math+sci+gym+his)/5
print("this is your average marks: ", avg)
if avg > 75:
    print("your grade is an A")
elif avg > 60:
    print("your grade is an B")
else:
    print("you have a C")