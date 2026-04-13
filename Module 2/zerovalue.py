try:

  num = int(input("enter a number"))
  num2 = int(input("enter another number"))
  print(num/num2)
except ValueError as e:
  print(e)
except ZeroDivisionError as e:
  print(e)

