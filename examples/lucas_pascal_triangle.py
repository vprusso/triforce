from triforce.triangles import LucasPascalTriangle, WythoffTriangle


triangle = WythoffTriangle(20)
print(triangle)
print(triangle.row_sums())
print(triangle.center())


print(triangle.rising_diagonal_sums())

print(triangle.diagonal(2, "right"))