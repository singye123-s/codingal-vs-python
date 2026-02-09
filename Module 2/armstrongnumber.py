number = int(input("enter a number to check: "))
temp = number
sum = 0
while temp > 0:
    digit = temp%10
    sum = digit ** 3
    temp = temp//10
if sum == number:
    print("armstrong")
else:
    print("not armstrong")