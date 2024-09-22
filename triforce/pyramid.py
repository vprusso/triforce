"""Primary Pyramid class."""


class Pyramid:
    def __init__(self, n: int):
        """Initialize the pyramid with n layers."""
        self.n = n
        self.pyramid = self.generate_pyramid()

    def __len__(self):
        return len(self.pyramid)

    def __getitem__(self, key):
        return self.pyramid[key]

    def __str__(self):
        return self.format_pyramid()

    def generate_pyramid(self) -> list[list[list[int]]]:
        """Generate the pyramid. This should be overridden by subclasses."""
        raise NotImplementedError("Subclasses should implement this method to generate specific pyramids.")

    def flatten(self) -> list[int]:
        """Flatten the pyramid into a 1D list."""
        return [item for layer in self.pyramid for row in layer for item in row]

    def layer_sums(self) -> list[int]:
        """Calculate the sum of each layer in the pyramid."""
        return [sum(sum(row) for row in layer) for layer in self.pyramid]

    def format_pyramid(self):
        """Format the pyramid for display as upside-down triangles with correct spacing."""
        ret = ""
        for n, layer in enumerate(self.pyramid):
            ret += f"Layer {n}:\n"
            max_width = len(str(max(max(row) for row in layer)))
            spacing = 3  # Adjust for readability
            last_row_width = len(layer[0]) * (max_width + spacing) - spacing  # Calculate width of the largest row

            # Reverse rows to print largest first and smallest last
            for _, row in enumerate(reversed(layer)):
                formatted_nums = [f"{num:^{max_width}}" for num in row]
                # Add padding for each row to keep the triangle shape upside down
                left_padding = (last_row_width - len(row) * (max_width + spacing) + spacing) // 2
                ret += " " * left_padding + (" " * spacing).join(formatted_nums) + "\n"

            ret += "\n"
        return ret
