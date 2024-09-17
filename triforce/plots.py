from typing import Callable

from triforce.triangle import Triangle
import matplotlib.pyplot as plt
import numpy as np


def highlight_plot(triangle: Triangle, filter_function: Callable):
    """Plot the triangle, highlighting numbers that satisfy the filter function."""
    n = triangle.n
    grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1):
            if filter_function(triangle[i][j]):
                grid[i, j] = 1

    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="binary", interpolation="none")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    from triforce.triangles import *
    from triforce.numeric import *

    n = 510
    triangle = PascalTriangle(n)
    highlight_plot(triangle, is_even)
