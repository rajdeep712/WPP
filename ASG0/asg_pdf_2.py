n=int(input("Enter the size of the array : "))
prices = []
for i in range(n):
    a=int(input(f"Enter price of day {i+1} : "))
    prices.append(a)

span = []
n=0

for i in prices:
    count=1
    if(n>0):
        for k in range(n-1,-1,-1):
            if(prices[k]<i):
                count+=1
            if(prices[k]>i):
                break
    span.append(count)
    n+=1

print(span)