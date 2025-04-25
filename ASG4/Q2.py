def is_square_int(n):
    x= int(n**0.5)
    if(x**2 == n):
        return True
    else:
        return False

times=int(input(""))
lst=[]
for i in range(times):
    a=input("")
    lst.append(a)

for numbers in lst:
    nums = numbers.split(" ")
    i=int(nums[0])
    j=int(nums[1])
    count=0
    for k in range(i,j+1):
        if(is_square_int(k)):
            count += 1
    print(count)