from triforce.pyramid import Pyramid
from triforce.sequences import fibonacci
from triforce.numeric import trinomial


class PascalPyramid(Pyramid):
    def generate_pyramid(self) -> list[list[list[int]]]:
        """Generate Pascal's Pyramid up to n layers."""
        pyramid = []
        for n in range(self.n):
            layer = []
            for i in range(n + 1):
                row = [trinomial(n, i, j) for j in range(n - i + 1)]
                layer.append(row)
            pyramid.append(layer)
        return pyramid


class HosoyaPyramid(Pyramid):
    def generate_pyramid(self) -> list[list[list[int]]]:
        """Generate Hosoya's Pyramid up to n layers."""
        pyramid = []
        for i in range(self.n):
            layer = []
            for j in range(i + 1):
                row = [fibonacci(i + 1) * fibonacci(j + 1) * fibonacci(k + 1) for k in range(i - j + 1)]
                layer.append(row)
            pyramid.append(layer)
        return pyramid
