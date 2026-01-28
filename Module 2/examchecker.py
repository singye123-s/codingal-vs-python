medical = str(input(" Do you have a medical condition?: "))

if medical == "Y":
    print("your are allowed into the exam!")
elif medical == "N":
    attendance = float(input("enter your attendance percent: "))
    if attendance >= 75:
        print("you are allowed!")
    else:
        print("you re not eligible for the exam!!!")

