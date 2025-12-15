math = float(input("enter your score out of 100: "))
science = float(input("enter your score out of 100: "))
hindi = float(input("enter your score out of 100: "))
english = float(input("enter your score out of 100: "))
totalmarks= math+science+hindi+english

per=(totalmarks/400)*100
print("overall percentage is:", per,"%!")
p = int(per)
print(p)