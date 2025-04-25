import pandas as pd

john = [True,True,False,True,False,False,False,True,True,True]
judy = [False,True,True,True,False,False,True,True,False,True]
df = pd.DataFrame({"john":john,"judy":judy})

days_till_party = []
count=0
for i in range(9,-1,-1):
    if john[i] and judy[i]:
        count = 0
        days_till_party.append(count)
    else:
        count+=1
        days_till_party.append(count)
days_till_party.reverse()

df["days_til_party"] = days_till_party

print(df)