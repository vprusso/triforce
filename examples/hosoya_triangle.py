from triforce.triangles import HosoyaTriangle


triangle = HosoyaTriangle(10)
print(triangle)

# Extract the right-most diagonal of the triangle
print(triangle.diagonal(diagonal_index=0, direction="right"))

# Extract the left-most diagonal of the triangle
print(triangle.diagonal(diagonal_index=0, direction="left"))

# Extract the middle entries of the triangle
print(triangle.middle_entries())