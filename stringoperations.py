#string operations
name1 = str(input("whats your first name?" ))
name2 = str(input("whats your last name?" ))
print(name1 +" "+ name2)
length1 = len(name1)
print(length1)


print(name1.upper())
print(name1.lower())
reverse = name2[::-1]
print(reverse)
ch = name1[length1-1]
print(ch)
