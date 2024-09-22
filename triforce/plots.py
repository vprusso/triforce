"""Plotting for triangles and pyramids."""
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np

from triforce.triangle import Triangle
from triforce.triangles import LucasPascalTriangle
from triforce.numeric import is_even


def highlight_plot(input_triangle: Triangle, filter_function: Callable):
    """Plot the triangle, highlighting numbers that satisfy the filter function."""
    n = input_triangle.n
    grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1):
            if filter_function(input_triangle[i][j]):
                grid[i, j] = 1

    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="binary", interpolation="none")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    highlight_plot(LucasPascalTriangle(n=510), is_even)
