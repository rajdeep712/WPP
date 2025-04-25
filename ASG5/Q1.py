L=int(input(""))
R=int(input(""))
lst=[i^j for i in range(L,R+1) for j in range(i,R+1)]
print(max(lst))