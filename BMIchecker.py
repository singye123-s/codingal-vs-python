height = float(input("enter height in cm: "))
weight= float(input("enter weight in kg: "))
BMI=weight/(height/100)**2
if BMI <= 18.5:
    print("you are underweight!")
    print(BMI)
elif BMI <= 25:
    print("you are healthy!")
    print(BMI)
elif BMI < 30:
     print("you're overweight!")
     print(BMI)
else:
    print("you are obese!")