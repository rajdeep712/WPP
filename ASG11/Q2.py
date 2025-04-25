import pandas as pd

s = pd.Series(['X','Y','T','Aaba','Baca','CABA',None,'bird','horse','dog'])
results = [(s[i].upper(),s[i].lower(),len(s[i])) for i in range(len(s)) if s[i] is not None]

for result in results:
    print(result[0],",",result[1],end=" ")
    print(",length=",result[2])