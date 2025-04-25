cases = int(input(""))
lst=input("").split(" ")
for i in range(cases):
    if(int(lst[i]) % 2 == 0) :
        ver = hor = int(int(lst[i])/2)
        print(ver*hor)
    
    else:
        ver = int(int(lst[i])/2)
        hor = ver+1
        print(hor*ver) 