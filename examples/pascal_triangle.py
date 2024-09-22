"""Properties of Pascal's triangle."""
from triforce.triangles import PascalTriangle
triangle = PascalTriangle(10)

# Print the output as a triangular shape:
print(triangle)

# Extract the right-most diagonal of the triangle:
print(triangle.diagonal(diagonal_index=0, direction="right"))

# Extract the second-to-the-right-most diagonal of the triangle:
print(triangle.diagonal(diagonal_index=1, direction="right"))

# Extract the center entries of the triangle:
print(triangle.center())

# Extract row sums:
print(triangle.row_sums())