from triforce.triangles import PascalTriangle
import matplotlib.pyplot as plt
import numpy as np


def sierpinski_from_pascals(n_rows):
    """Generate a grid of values 0 (even) and 1 (odd) based on Pascal's triangle."""
    pascals_triangle = PascalTriangle(n_rows).generate_triangle()
    grid = np.zeros((n_rows, n_rows), dtype=int)
    for i in range(n_rows):
        for j in range(i + 1):
            grid[i, j] = pascals_triangle[i][j] % 2  # 1 for odd, 0 for even
    return grid

def plot_sierpinski(grid):
    """Plot the Sierpinski triangle pattern using matplotlib."""
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap='binary', interpolation='none')  # 'binary' colormap: 0 -> black, 1 -> white
    plt.axis('off')  # Turn off axes for a cleaner look
    plt.show()

# Example usage
n_rows = 64  # Number of rows in Pascal's triangle
sierpinski_grid = sierpinski_from_pascals(n_rows)
plot_sierpinski(sierpinski_grid)
