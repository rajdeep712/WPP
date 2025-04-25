def chech_fibo(num):
    i=0
    while(True):
        if(fibo(i) == num):
            return True
        if(fibo(i)>num):
            return False
        i+=1

def fibo(a):
    if(a==0):
        return 0
    if(a==1):
        return 1
    return fibo(a-1)+fibo(a-2)

n = int(input("Enter the number of test cases : "))
lst = []
for i in range(n):
    a=int(input("Enter number : "))
    lst.append(a)

for j in lst:
    check=chech_fibo(j)
    if(check):
        print("IsFibo")
    else:
        print("IsNotFibo")