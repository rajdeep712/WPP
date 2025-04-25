n = int(input("Enter the number of test cases : "))
lst = []
for i in range(n):
    lst.append(input("Enter number {} : ".format(i+1)))

for num in lst:
    count = 0
    for j in num:
        if(int(num) % int(j) == 0):
            count += 1
    print(count)