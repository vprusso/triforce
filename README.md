triforce
=====================
![PyPI - downloads](https://img.shields.io/pypi/dm/triforce.svg?label=Pypi%20downloads)

**Contents**
- [triforce](#triforce)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [Team](#team)
  - [Citing](#citing)

Triforce is suite of tools for the numerical exploration of triangular arrays. It allows you to manipulate well-known
triangular arrays (i.e. Pascal's triangle, the Hosoya triangle, Bell's triangle, etc.) and also to define your own
triangle via specifying generating functions.

For example, the following code allows you to define the [Hosoya
Triangle](https://en.wikipedia.org/wiki/Hosoya%27s_triangle) for a given number of rows. You can use the functionality
of triforce to investigate various numerical properties of the triangle.

```python3
>>> from triforce.triangles import HosoyaTriangle
>>> triangle = HosoyaTriangle(10)
>>> 
>>> # Print the output as a triangular shape:
>>> print(triangle)
                      1
                    1    1
                 2    1    2
               3    2    2    3
            5    3    4    3    5
          8    5    6    6    5    8
       13   8    10   9    10   8    13
     21   13   16   15   15   16   13   21
  34   21   26   24   25   24   26   21   34
55   34   42   39   40   40   39   42   34   55

>>> # Extract the right-most diagonal of the triangle
>>> print(triangle.diagonal(diagonal_index=0, direction="right"))
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

>>> # Extract the second-to-the-right-most diagonal of the triangle
>>> print(triangle.diagonal(diagonal_index=1, direction="right"))
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

>>> # Extract the middle entries of the triangle
>>> print(triangle.middle_entries())
[1, 1, 4, 9, 25]
```

You can also define your own triangular array by creating a class that inherits from the `Triangle` class

```python3
from triforce.triangle import Triangle

class WythoffTriangle(Triangle):
    def __init__(self, n: int, recurrence_function=None):
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
```

One can also visualize properties of the triangles by plotting. Here is an example of visualizing Pascal's triangle such
that the even and odd terms are replaced by black and white pixels, respectively.

```python3
triangle = PascalTriangle(n=400)
even_odd_plot(triangle)
```

![even-odd plot for Pascal's triangle](https://github.com/vprusso/triforce/tree/master/static/pascal_even_odd_plot.png)


## Installation
Triforce is available on PyPI, and can be installed with
```
pip install triforce
```

## Contributing
We appreciate all contributions. You don't need to be an expert in triangular arrays or number theory to help out.

Contributions should be submitted as [pull requests](https://github.com/vprusso/triforce/pulls).  A member of the
triforce development team will review the pull request and guide you through the contributing process.

## Team
Triforce is a community project, built from the contributions of many researchers and engineers. Triforce is developed
and maintained by [Vincent Russo](https://vprusso.github.io/)

## Citing

You can cite `triforce` using the following DOI: X


If you are using the `triforce` software package in research work, please include an explicit mention of `triforce` in
your publication. Something along the lines of:

```
To solve problem "X" we used `triforce`; a package for studying numerical properties of triangular arrays.
```

A BibTeX entry that you can use to cite `triforce` is provided here:

```bib
@misc{triforce,
   author       = {Vincent Russo},
   title        = {triforce: A {P}ython toolkit for numerical analysis of triangular arrays},
   howpublished = {\url{https://github.com/vprusso/triforce}},
   month        = Dec,
   year         = 2024,
   doi          = {X}
 }
```
