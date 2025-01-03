triforce
=========
The `triforce` package is suite of tools for the numerical exploration of
triangular arrays. It allows you to manipulate well-known triangular arrays
(i.e. Pascal's triangle, the Hosoya triangle, Bell's triangle, etc.) and also
to define your own triangle via specifying generating functions.

For example, the following code allows you to define Pascal's Triangle for a
given number of rows. You can use the functionality of `triforce` to
investigate various numerical properties of the triangle.

```python3
>>> from triforce.triangles import PascalTriangle
>>> triangle = PascalTriangle(10)
>>> 
>>> # Print the output as a triangular shape:
>>> print(triangle)
                           1 
                         1     1 
                      1     2     1 
                   1     3     3     1 
                1     4     6     4     1 
             1     5    10    10     5     1 
          1     6    15    20    15     6     1 
       1     7    21    35    35    21     7     1 
    1     8    28    56    70    56    28     8     1 
 1     9    36    84    126   126   84    36     9     1 

>>> # Extract the right-most diagonal of the triangle:
>>> print(triangle.diagonal(diagonal_index=0, direction="right"))
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

>>> # Extract the second-to-the-right-most diagonal of the triangle:
>>> print(triangle.diagonal(diagonal_index=1, direction="right"))
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> # Extract the center entries of the triangle:
>>> print(triangle.center())
[1, 2, 6, 20, 70]

>>> # Extract row sums:
>>> print(triangle.row_sums())
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

```

You can also define your own triangular array by creating a class that inherits
from the `Triangle` class

```python3
from triforce.triangle import Triangle

class WythoffTriangle(Triangle):
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
```

One can also visualize properties of the triangles by plotting. Here is an
example of visualizing Pascal's triangle such that the even and odd terms are
replaced by black and white pixels, respectively.

```python3
from triforce.plots import highlight_plot
from triforce.numerics import is_even

highlight_plot(PascalTriangle(n=510), is_even)
```

![even-odd plot for Pascal's triangle](./static/pascal_parity_plot.png)
