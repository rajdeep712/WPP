from abc import abstractmethod,ABC

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return format(3.14 * self.radius * self.radius , "<10.2f")
    
    def perimeter(self):
        return format(2 * 3.14 * self.radius , "<10.2f")
    
class Reactangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return format(self.length * self.breadth , "<10.2f")
    
    def perimeter(self):
        return format(2*(self.length + self.breadth) , "<10.2f")
    

r1 = Reactangle(12.3,24.9)
print(r1.area())
print(r1.perimeter())

c1 = Circle(2.54)
print(c1.area())
print(c1.perimeter())