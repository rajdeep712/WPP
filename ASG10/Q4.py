import numpy as np
# from numpy import random
import math

points = np.random.randint(30,size=(11,2))
print(points)

polar_coordinates = np.array([f"{(point[0]**2+point[1]**2)**0.5},{math.atan(point[1]/point[0])}" if point[0]!=0 else f"{(point[1]**2)**0.5},undefined" for point in points])

print(polar_coordinates)