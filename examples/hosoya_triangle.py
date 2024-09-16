from triforce.triangles import HosoyaTriangle


triangle = HosoyaTriangle(10)
print(triangle)

print(triangle.diagonal(diagonal_index=0))

print(triangle.row_sums())