"""Lucas-Pascal triangle example."""
from triforce.triangles import LucasPascalTriangle


triangle = LucasPascalTriangle(20)
print(triangle)
print(triangle.row_sums())
print(triangle.center())


print(triangle.rising_diagonal_sums())

print(triangle.diagonal(2, "right"))
