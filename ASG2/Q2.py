prices = {}
while(True):
    pro_name = input("Enter the product name : ")
    price = float(input("Enter the price of the product : "))
    prices.update({pro_name:price})
    a=input('''Do you want to enter more products,
If yes, Enter \'Y\' else Enter \'N\' : ''')
    if(a == 'N'):
        break

print("To get the prices-")
while(True):
    inp = input("Enter a product name : ")
    if(prices.get(inp) == None):
        print("Item not found")
    else:
        print(f"price is {prices.get(inp)}")

    b=input('''Do you want to know prices of more products,
If yes, Enter \'Y\' else Enter \'N\' : ''')
    
    if(b == 'N'):
        break