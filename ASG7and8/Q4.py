class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __add__(self,other):
        return self.salary + other.salary
    def __sub__(self,other):
        if(self.salary > other.salary):
            return f'{self.name} has more salary than {other.name}'
        else:
            return f'{other.name} has more salary than {self.name}'

    
a=Employee('Yadhav',1572.34)
b=Employee('Subhman',3489.59)

print(format((a+b) , "<10.2f"))
print(a-b)