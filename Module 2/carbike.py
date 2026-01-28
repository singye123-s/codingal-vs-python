vehicle = int(input("what vehicle would you like to use: Bike.1 or Car.2: "))
if vehicle == 1:
 subbike = int(input("what type of bike: Scootie.1, electric.2, motorcyle.3"))
 if subbike == 1:
  print("you have selected a scootie")
 elif subbike == 2:
  print("you have selected a electric bike")
 elif subbike == 3:
  print("you have selected motorcycle")
else:
 subcar = int(input("what type of car: electric car.1, SUV.2, sportscar.3"))
 if subcar == 1:
  print("you have selected a electric car")
 elif subcar == 2:
  print('you have selected SUV')
 elif subcar == 3:
  print("you have selected sportscar")