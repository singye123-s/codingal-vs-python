
num = input("Enter a number: ")


if num[0] == '-':
    num = num[1:]

count = 0


for digit in num:
    count = count + 1

print("Total digits:", count)
