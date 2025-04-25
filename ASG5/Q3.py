import sys

cases = int(input(""))
lst = [input("") for i in range(cases)]
for word in lst:
    new = ""
    check=0
    for idx in range(len(word)-1,0,-1):
        if(word[idx]>word[idx-1]):
            new += word[idx]
            new += word[idx-1]
            check=1
            break
        else:
            new = word[idx]+new
    if(check == 0):
        print("no answer")
        continue
    for j in range(idx-2,-1,-1):
        new = word[j]+new
    
    print(new)