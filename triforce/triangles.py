from triforce.sequences import (
    fibonacci,
    lower_wythoff,
    upper_wythoff,
)


class Triangle:
    def __init__(self, n: int):
        """Initialize the triangle with n rows."""
        self.n = n
        self.triangle = self.generate_triangle()

    def __len__(self):
        return len(self.triangle)

    def __getitem__(self, key):
        return self.triangle[key]

    def __str__(self):
        return self.format_triangle()

    def generate_triangle(self) -> list[list[int]]:
        """Generate the triangle. This should be overridden by subclasses."""
        raise NotImplementedError("Subclasses should implement this method to generate specific triangles.")

    def flatten(self) -> list[int]:
        """Flatten the triangle into a 1D list."""
        return [item for row in self.triangle for item in row]

    def row_sums(self) -> list[int]:
        """Calculate the sum of each row in the triangle."""
        return [sum(row) for row in self.triangle]

    def column_sums(self) -> list[int]:
        """Calculate the sum of each column in the triangle."""
        max_col = len(self.triangle[-1])
        sums = [0] * max_col
        for row in self.triangle:
            for i, val in enumerate(row):
                sums[i] += val
        return sums

    def row_differences(self) -> list[list[int]]:
        """Calculate the difference between consecutive rows in the triangle."""
        differences = []
        for i in range(1, len(self.triangle)):
            diff = [self.triangle[i][j] - self.triangle[i-1][j] for j in range(len(self.triangle[i-1]))]
            differences.append(diff)
        return differences

    def cumulative_row_sums(self) -> list[int]:
        """Calculate cumulative sums of each row in the triangle."""
        row_sums = self.row_sums()
        return [sum(row_sums[:i+1]) for i in range(len(row_sums))]

    def diagonal_sums(self, direction: str = 'right') -> list[int]:
        """Calculate the sum of the diagonals in the triangle."""
        max_diags = len(self.triangle)
        sums = []
        for diag_num in range(max_diags):
            diagonal = self.diagonal(diag_num, direction)
            sums.append(sum(diagonal))
        return sums

    def parity_pattern(self) -> list[list[int]]:
        """Generate a parity pattern where 1 represents odd numbers and 0 represents even numbers."""
        return [[1 if val % 2 == 1 else 0 for val in row] for row in self.triangle]

    def mod_triangle(self, k: int) -> list[list[int]]:
        """Calculate the triangle with entries modulo k."""
        return [[val % k for val in row] for row in self.triangle]

    def is_symmetric(self) -> bool:
        """Check if the triangle is symmetric."""
        for row in self.triangle:
            if row != row[::-1]:
                return False
        return True

    def diagonal(self, diagonal_index: int, direction: str = "right") -> list[int]:
        """Extract the diagonal as a list of elements.

        Args:
            diagonal_index (int): The index of the diagonal to extract.
            direction (str): Either 'left' or 'right', indicating the diagonal's direction.

        Returns:
            list[int]: A list of elements from the specified diagonal.
        """
        diagonal = []

        if direction == "right":
            # Extract the right diagonal (down-right from left edge)
            for i in range(diagonal_index, len(self.triangle)):
                diagonal.append(self.triangle[i][diagonal_index])
        elif direction == "left":
            # Extract the left diagonal (down-left from right edge)
            for i in range(len(self.triangle) - diagonal_index):
                diagonal.append(self.triangle[i + diagonal_index][i])
        else:
            raise ValueError("Direction must be either 'left' or 'right'.")

        return diagonal

    def format_triangle(self, highlight_diag=None, highlight_shape=None):
        """Format the triangle for printing with options to highlight specific diagonals or shapes."""
        def is_in_diagonal(row, col, diag):
            return (row - col == diag) or (col - row == diag)

        def highlight_element(num):
            return f"\033[1m{num}\033[0m"  # Bold text (ANSI escape code)

        max_width = len(str(max(max(row) for row in self.triangle)))
        spacing = 3  # Adjust for readability
        last_row_width = len(self.triangle[-1]) * (max_width + spacing) - spacing

        ret = ""
        for i, row in enumerate(self.triangle):
            formatted_nums = []
            for j, num in enumerate(row):
                if highlight_diag is not None and is_in_diagonal(i, j, highlight_diag):
                    formatted_nums.append(f"{highlight_element(num):^{max_width}}")
                else:
                    formatted_nums.append(f"{num:^{max_width}}")
            left_padding = (last_row_width - len(row) * (max_width + spacing) + spacing) // 2
            ret += " " * left_padding + (" " * spacing).join(formatted_nums) + "\n"
        return ret


class HosoyaTriangle(Triangle):
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
