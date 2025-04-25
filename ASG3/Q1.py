inp = input("Enter a number : ")
while(len(inp) != 1):
    temp = 0
    for i in inp:
        temp += int(i)
    inp = str(temp)

print("The digital root is",inp)