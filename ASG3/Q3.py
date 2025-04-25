times = int(input(""))
lst=[]
for i in range(times):
    a=int(input(""))
    lst.append(a)

for cycles in lst:
    height = 1
    for cycle in range(1,cycles+1):
        if(cycle%2 != 0):
            height *= 2
        elif(cycle%2 == 0):
            height += 1
    print(height)