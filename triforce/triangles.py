from triforce.sequences import (
    fibonacci,
    compound_wythoff,
    lower_wythoff,
    upper_wythoff,
)
from triforce.triangle import Triangle


class BellTriangle(Triangle):
    """Defines the Bell Triangle: https://en.wikipedia.org/wiki/Bell_triangle"""
    def generate_triangle(self) -> list[list[int]]:
        """Generate Bell's triangle up to row n."""
        triangle = [[1]]  # Initialize with the first row
        
        for i in range(1, self.n):
            row = [triangle[i-1][-1]]  # First element is the last element of the previous row
            for j in range(1, i + 1):
                row.append(row[-1] + triangle[i-1][j-1])
            triangle.append(row)
        return triangle


class CatalanTriangle(Triangle):
    """Defines Catalan's Triangle: https://en.wikipedia.org/wiki/Catalan%27s_triangle"""
    def generate_triangle(self) -> list[list[int]]:
        """Generate Catalan's triangle up to row n."""
        triangle = [[1]]  # Initialize with the first row
        
        for i in range(1, self.n):
            row = [1]  # The first element of each row is always 1
            for j in range(1, i + 1):
                row.append(triangle[i-1][j-1] + row[j-1])
            triangle.append(row)
        return triangle


class FloydsTriangle(Triangle):
    """Defines Floyd's Triangle: https://en.wikipedia.org/wiki/Floyd%27s_triangle"""
    def generate_triangle(self) -> list[list[int]]:
        """Generate Floyd's triangle up to row n."""
        triangle = []
        num = 1  # Start counting from 1
        
        for i in range(1, self.n + 1):
            row = []
            for _ in range(i):
                row.append(num)
                num += 1
            triangle.append(row)
        return triangle


class HosoyaTriangle(Triangle):
    """Defines the Hosoya Triangle: https://en.wikipedia.org/wiki/Hosoya%27s_triangle"""
    def generate_triangle(self) -> list[list[int]]:
        """Generate the Hosoya triangle up to row n."""
        triangle = []
        for i in range(self.n):
            row = []
            for j in range(i + 1):
                entry = fibonacci(j + 1) * fibonacci(i - j + 1)
                row.append(entry)
            triangle.append(row)
        return triangle


class PascalTriangle(Triangle):
    """Defines Pascal's Triangle: https://en.wikipedia.org/wiki/Pascal%27s_triangle"""
    def generate_triangle(self) -> list[list[int]]:
        """Generate Pascal's triangle up to row n."""
        triangle = [[1]]
        for i in range(1, self.n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle


class WythoffTriangle(Triangle):
    def __init__(self, n: int):
        """Initialize the Wythoff triangle with n rows and a custom recurrence function."""
        super().__init__(n)

    def generate_triangle(self) -> list[list[int]]:
        """Generate the Wythoff triangle up to row n using Fibonacci recurrence."""
        triangle = []

        for i in range(self.n):
            row = []
            
            # First element: lower Wythoff sequence
            if i == 0:
                row.append(0)  # Starting element for Wythoff triangle
            else:
                row.append(lower_wythoff(i))

            # Middle elements: Fill using Fibonacci recurrence
            for j in range(1, i):
                # Fibonacci recurrence: current element is the sum of the two elements above it
                row.append(triangle[i-1][j-1] + triangle[i-1][j])

            # Last element: upper Wythoff sequence
            if i > 0:
                row.append(upper_wythoff(i))

            triangle.append(row)

        return triangle
