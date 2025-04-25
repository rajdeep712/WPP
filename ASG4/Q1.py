times = int(input("Enter number of test cases : "))
lst=[]
for i in range(times):
    a=input("")
    lst.append(a)

for word in lst:
    count=0
    for i in range(1,(int(len(word)/2))+1):
        check=word[len(word)-i]
        while(check != word[i-1]):
            count += 1
            check = chr(ord(check)-1)

    print(count)