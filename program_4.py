#Matthew Tyler
#10/17/25
#Coordinates

import math

def calculate_distance():
    x1, y1, z1 = coordinate1
    x2, y2, z2 = coordinate2
    return math.sqrt ((x2-x1)**2 + (y2 - y1)**2 + (z1 - z2)**2)

coord_input1 = input("Please enter Coordinate 1 seperating each value with a space.")
coord_input2 = input("Please enter Coordinate 2 seperating each value with a space.")

coordinate1 = tuple(map(float, coord_input1.split()))
coordinate2 = tuple(map(float, coord_input2.split()))
distance = calculate_distance()
print("The distance from two points:", distance)
