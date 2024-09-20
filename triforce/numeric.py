"""Numeric properties."""


def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_even(num: int) -> bool:
    """Check if number is even."""
    return num % 2 == 0


def is_odd(num: int) -> bool:
    """Check if number is odd."""
    return num % 2 != 0


def trinomial(n: int, i: int, j: int) -> int:
    """Calculate the trinomial coefficient."""
    k = n - i - j
    if k < 0:
        return 0
    return factorial(n) // (factorial(i) * factorial(j) * factorial(k))


def factorial(num: int) -> int:
    """Calculate the factorial of a number."""
    if num in [0, 1]:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

