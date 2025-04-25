class BankAccount:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.avl_balance = balance


    def deposit(self,amount):
        self.avl_balance += amount
        print(f'{amount} deposited successfully')

    def withdrawl(self,amount):
        self.avl_balance -= amount
        print(f'{amount} withdrawn successfully')

    def display(self):
        print(f'Account no : {self.account_no} -->  Available balance : {self.avl_balance}')


cust1 =BankAccount('Rajdeep',1234)
cust2 =BankAccount('Rajdeep Paul',123)
cust3 =BankAccount('Raj',124)

cust1.deposit(56)
cust2.deposit(568)
cust1.display()