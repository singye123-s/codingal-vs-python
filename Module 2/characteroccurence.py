name = str(input("enter your name: "))
ch = str(input("enter character: "))
i = 0
count = 0
while i < len(name):
    if name[i] == ch:
        count = count+1
 
    i = i+1 

print(count)