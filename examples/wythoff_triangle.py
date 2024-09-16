from triforce.constants import PHI, PHI2
from triforce.triangles import *
from math import floor


triangle = WythoffTriangle(10)
print(triangle)

print(triangle.diagonal(1, "right"))

print(triangle.middle_entries())

#n = 10
#print([sum([floor(k * PHI2) for k in range(i)]) + 1 for i in range(1, n)])
#print(triangle.diagonal(1, "left"))
#
#print([sum([floor(k * PHI) for k in range(i)]) + 2 for i in range(1, n)])
#print(triangle.diagonal(1, "right"))
# Example usage for Bell's triangle