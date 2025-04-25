import re
x=set()
for i in range(97,123):
    x.add(chr(i))
pattern = r"[a-z]"
s=input("Enter the string : ")
s_=s.lower()
words=set(re.findall(pattern,s_))

if(words == x):
    print("pangram")
else:
    print("Not pangram")