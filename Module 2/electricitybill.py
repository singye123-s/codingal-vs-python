units = float(input("enter your amount of units consumed: "))
if units <= 50:
    bill = (units * 2.60) +25
    
elif 50 < units < 100:
    bill = (units * 3.25) + 35
    
elif 100 < units < 200:
    bill = (units * 5.26) + 45
    
else:
    bill= (units * 8.45) + 75
    
print("you total bill is!!", bill)