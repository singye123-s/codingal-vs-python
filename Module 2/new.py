try:
   num1 = int(input("emter num"))
   num2 = int(input("enter another num"))
   print(num1/num2)
except ZeroDivisionError as e:
   print(e)
except ValueError as e:
   print(e)

