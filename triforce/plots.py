from triforce.triangle import Triangle
import matplotlib.pyplot as plt
import numpy as np


def even_odd_plot(triangle: Triangle):
    """Generate a grid of values 0 (even) and 1 (odd) based on triangle."""
    n = triangle.n
    grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1):
            grid[i, j] = triangle[i][j] % 2  # 1 for odd, 0 for even

    plt.figure(figsize=(6, 6))
    # 'binary' colormap: 0 -> black, 1 -> white
    plt.imshow(grid, cmap="binary", interpolation="none")
    # Turn off axes for a cleaner look
    plt.axis("off")
    plt.show()

#n = 400
#triangle = PascalTriangle(n)
#even_odd_plot(triangle)
