"""Primary Triangle class."""

class Triangle:
    """Base Triangle class."""
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

    def rising_diagonal(self, row_index: int) -> list[int]:
        """Extract the rising diagonal starting from the leftmost element of the specified row."""
        diagonal = []
        row, col = row_index, 0  # Start at the leftmost element of the specified row

        # Traverse diagonally up-right
        while row >= 0 and col < len(self.triangle[row]):
            diagonal.append(self.triangle[row][col])
            row -= 1  # Move up
            col += 1  # Move right

        return diagonal

    def rising_diagonal_sums(self) -> list[int]:
        """Calculate the sum of the elements in each rising diagonal."""
        sums = []
        for i in range(self.n):
            diag = self.rising_diagonal(i)
            sums.append(sum(diag))
        return sums

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

    def center(self) -> list[int]:
        """Return the middle entries for rows with an odd number of elements."""
        middle_entries = []
        for row in self.triangle:
            if len(row) % 2 == 1:
                # Row has an odd number of elements, so get the middle element
                middle_index = len(row) // 2
                middle_entries.append(row[middle_index])
        return middle_entries

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

    def format_triangle(self, highlight_diag=None):
        """Format the triangle for printing with options to highlight specific diagonals or shapes."""
        def is_in_diagonal(row, col, diag):
            return diag in (row - col, col - row)

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
