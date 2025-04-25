import pandas as pd

data={
    'date':['2025-05-17', '2025-04-21','2025-07-28','2025-07-29','2025-05-05'],
    'artist':['A','B','A','C','B'],
    'venue':['X','X','Y','Y','Z']
}

df=pd.DataFrame(data)
df['date']=pd.to_datetime(df['date'])
df['year_month']=df['date'].dt.to_period('M')
df['pair']=df['artist']+'_'+df['venue']


pivot=df.pivot_table(index='year_month', columns='pair', aggfunc='size', fill_value=0)
artists=df['artist'].unique()
venues=df['venue'].unique()
all_pairs=[f"{a}_{v}" for a in artists for v in venues]

for pair in all_pairs:
    if pair not in pivot.columns:
        pivot[pair]=0

pivot=pivot[all_pairs]

print(pivot)