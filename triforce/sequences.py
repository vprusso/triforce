"""Integer sequences used to generate triangular arrays."""

from math import floor
from triforce.constants import PHI, PHI2


def fibonacci(n: int) -> int:
    """OEIS-A000045: Generate n-th Fibonacci number."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


def tribonacci(n: int) -> int:
    """Generate the n-th Tribonacci number."""
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 0 if n == 1 else 1

    a, b, c = 0, 0, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c


def lucas(n: int) -> int:
    """OEIS-A000032: Generate nth Lucas number."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


def pell(n: int) -> int:
    """OEIS-A000129: Generate nth Pell number."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, 2 * b + a
    return b


def pell_lucas(n: int) -> int:
    """OEIS-A002203: Generate nth Pell-Lucas number."""
    if n == 0:
        return 2
    if n == 1:
        return 2
    a, b = 2, 2
    for _ in range(2, n+1):
        a, b = b, 2 * b + a
    return b


def catalan(n: int) -> int:
    """OEIS-A000108: Generate nth Catalan number."""
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-1-i)
    return res


def lower_wythoff(n: int):
    """OEIS-A000201: Generate the n-th term of the lower Wythoff sequence."""
    return floor(n * PHI)


def upper_wythoff(n: int):
    """OEIS-A001950: Generate the n-th term of the upper Wythoff sequence."""
    return floor(n * PHI2)


def compound_wythoff(n: int):
    """OEIS-A003622: Generate the n-th term of the compound Wythoff sequence."""
    return floor(n * PHI2) - 1


def wythoff_term(n: int, k: int) -> int:
    """OEIS-:"""
    return (n - 1) * fibonacci(k) + fibonacci(k + 1) * floor(n * PHI)