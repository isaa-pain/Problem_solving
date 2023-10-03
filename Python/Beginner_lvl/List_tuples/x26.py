# Description:
# 1-Write a Python program that calculates the distance between two 3D points.
# 2-The points are represented by two lists with three elements. The first element is the x-coordinate. The second element is the y-coordinate. The third element is the z-coordinate.
# Formula to find the Distance:
# you may consider all points have 3-d coordinations (x,y,z), represented as a list
#  AB=sqrt((x2-x1)^2+(y2-y1)^2+(z2-z1)^2)

import math
point_a =[3,4,5]
point_b=[1,3,5]

distance_ab=math.sqrt((point_b[0]-point_a[0])**2+(point_b[1]-point_a[1])**2+(point_b[2]-point_a[2])**2)

print(distance_ab)