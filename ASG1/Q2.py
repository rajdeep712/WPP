from random import randint
lst=[]
for i in range(100):
    a=randint(0,1)
    lst.append(a)

print("The list is :",lst)
maximum=-1
count=0
for i in lst:
    if(i==0):
        count+=1
    else:
        if(count>maximum):
            maximum=count
        count=0

if(count>maximum):
    maximum=count

print("The longest run of zeros is : {}".format(maximum))