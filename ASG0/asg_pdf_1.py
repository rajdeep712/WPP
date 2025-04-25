test1={"Dhoni":74 , "Kohli":150 , "Sachin":0}
test2={"Dhoni":29 , "Kohli":0 , "Sachin":143}

total={}
for i in test1:
    total.update({i:test1[i]+test2[i]})

reversed_total={}
for i in test1:
    reversed_total.update({(test1[i]+test2[i]):i})

dhoni=total["Dhoni"]
kohli=total["Kohli"]
sachin=total["Sachin"]
max_runs=max(dhoni,max(kohli,sachin))

print(f"{reversed_total[max_runs]} is the orange cap winner with {max_runs} runs")