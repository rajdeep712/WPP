lst=[]
for i in range(10):
    temp=[]
    print("For point",i+1)
    a=int(input("X : "))
    temp.append(a)
    a=int(input("Y : "))
    temp.append(a)
    a=int(input("Z : "))
    temp.append(a)

    lst.append(temp)

closest_point=[]

for index,point in enumerate(lst):
    min_dist=999999999999999999
    track=-1
    for i,temp in enumerate(lst):
        if(i != index):
            dist=((point[0]-temp[0])**2)+((point[1]-temp[1])**2)+((point[2]-temp[2])**2)
            if(dist<min_dist):
                min_dist=dist
                track=i
        
    closest_point.append((point,lst[track]))

print("The input points are : ",lst)
print("The closest points corresponding to each point : ",closest_point)