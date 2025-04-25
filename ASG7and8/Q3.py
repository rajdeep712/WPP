class Bank:
    def __init__(self,name):
        self.name = name

    class Customer:
        def __init__(self,name,balance):
            self.cust_name = name
            self.avl_balance = balance

        def deposit(self,amount):
            self.avl_balance += amount
            print(f'Customer name : {self.cust_name} -->  Available balance : {self.avl_balance}')

        def withdrawl(self,amount):
            self.avl_balance -= amount
            print(f'Customer name : {self.cust_name} --> Available balance : {self.avl_balance}')


SBI = Bank('SBI')
cust1 = SBI.Customer('Rajdeep',1234)
cust2 = SBI.Customer('Rajdeep Paul',123)
cust3 = SBI.Customer('Raj',124)

cust1.deposit(56)
cust2.deposit(568)