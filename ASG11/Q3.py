import pandas as pd

asking_prices = pd.Series([20000,25000,18000,30000,22000])
fair_prices = pd.Series([22000,14000,19000,32000,21000])

good_deals = [index for index in range(len(asking_prices)) if fair_prices[index]>asking_prices[index]]

print("Indices with good deals are")
print(good_deals)