lst={i for i in range(1,10001)}
a=set()
b=set()
c=set()
d=set()
e=set()
for j in lst:
    if(j%5 == 0):
        a.add(j)
    elif(j%5 == 1):
        b.add(j)
    elif(j%5 == 2):
        c.add(j)
    elif(j%5 == 3):
        d.add(j)
    elif(j%5 == 4):
        e.add(j)

u=a.union(b,c,d,e)
if(u == lst):
    print("YES the union of all equivalence classes is the original list")
else:
    print("The union of all equivalence classes is not the original list")

# print(u)