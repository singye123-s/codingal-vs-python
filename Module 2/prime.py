lower= int(input("enter a number : "))
upper= int(input("enter a number : "))
for num in range(lower,upper+1,1):
    if num>1:
       for i in range (2,num,1):
        if num%i == 0:
           break
       else:
          print(num)