import math

class Vectors:
    class TwoDim:
        def __init__(self , x , y):
            self.x = x
            self.y = y
            self.z = 0

        def magnitude(self):
            self.magnitude = pow((self.x ** 2+self.y ** 2+self.z ** 2) , 0.5)
            print(f'Magnitude of the vactor is {self.magnitude}')

        def rotation(self,angle):
            angle = math.radians(angle)
            self.x = self.x * math.cos(angle) - self.y * math.sin(angle)
            self.y = self.y * math.cos(angle) + self.x * math.sin(angle)
            print(f'After rotation around X-axis, the vector becomes : {self.x}X + {self.y}Y.')


    class ThreeDim(TwoDim):
        def __init__(self,x,y,z):
            super().__init__(x,y)
            self.z = z
        
        # MAGNITUDE already declared above

        def rotation(self, angle):
            new_y = self.y * math.cos(angle) - self.z * math.sin(angle)
            new_z = self.y * math.sin(angle) + self.z * math.cos(angle)
            self.y = new_y
            self.z = new_z
            print(f'After rotation around X-axis, the vector becomes : {self.x}X + {self.y}Y + {self.z}Z.')

    @staticmethod
    def distance(v1,v2):
        dist = pow((v1.z - v2.z)**2 + (v1.y - v2.y)**2 + (v1.x - v2.x)**2 , 0.5)
        print(f'The distance between the two vectors is : {dist}')

    @staticmethod
    def dotproduct(v1,v2):
        result = (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)
        print(f'The distance between the two vectors is {result}')

    @staticmethod
    def crossproduct(v1, v2):
        cross_x = v1.y * v2.z - v1.z * v2.y
        cross_y = v1.z * v2.x - v1.x * v2.z
        cross_z = v1.x * v2.y - v1.y * v2.x
        if cross_z == 0:
            print(f'The cross product of the two vectors is: {cross_x}i + {cross_y}j')
            return
        print(f'The cross product of the two vectors is: {cross_x}i + {cross_y}j + {cross_z}k')
        return

a = Vectors.ThreeDim(1,2,3)
b = Vectors.ThreeDim(1,2,4)
a.magnitude()
Vectors.distance(a,b)
Vectors.dotproduct(a,b)
a.rotation(45)
Vectors.crossproduct(a,b)
c = Vectors.TwoDim(3,4)
d = Vectors.TwoDim(9,8)
c.magnitude()
d.magnitude()
d.rotation(90)
Vectors.crossproduct(c,d)
Vectors.dotproduct(c,d)
Vectors.distance(c,d)