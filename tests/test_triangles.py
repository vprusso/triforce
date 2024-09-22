"""Tests for triangle implementations."""
from triforce.triangles import (
    BellTriangle,
    CatalanTriangle,
    FloydsTriangle,
    HosoyaTriangle,
    PascalTriangle,
    FibonacciPascalTriangle,
    LucasPascalTriangle,
    WythoffTriangle
)


def test_bell_triangle():
    """Tests for Bell Triangle."""
    bell_triangle = BellTriangle(5)
    expected = [
        [1],
        [1, 2],
        [2, 3, 5],
        [5, 7, 10, 15],
        [15, 20, 27, 37, 52]
    ]
    assert bell_triangle.triangle == expected


def test_catalan_triangle():
    """Tests for Catalan Triangle."""
    catalan_triangle = CatalanTriangle(4)
    expected = [
        [1],
        [1, 1],
        [1, 2, 2],
        [1, 3, 5, 5]
    ]
    assert catalan_triangle.triangle == expected


def test_floyds_triangle():
    """Tests for Floyd Triangle."""
    floyd_triangle = FloydsTriangle(4)
    expected = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    assert floyd_triangle.triangle == expected


def test_hosoya_triangle():
    """Tests for Hosoyoa Triangle."""
    hosoya_triangle = HosoyaTriangle(5)
    expected = [
        [1],
        [1, 1],
        [2, 1, 2],
        [3, 2, 2, 3],
        [5, 3, 4, 3, 5]
    ]
    assert hosoya_triangle.triangle == expected


def test_pascal_triangle():
    """Tests for Pascal Triangle."""
    pascal_triangle = PascalTriangle(5)
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    assert pascal_triangle.triangle == expected


def test_fibonacci_pascal_triangle():
    """Tests for Fibonacci-Pascal Triangle."""
    fib_pascal_triangle = FibonacciPascalTriangle(5)
    expected = [
        [1],
        [1, 1],
        [2, 2, 2],
        [3, 4, 4, 3],
        [5, 7, 8, 7, 5]
    ]
    assert fib_pascal_triangle.triangle == expected


def test_lucas_pascal_triangle():
    """Tests for Lucas-Pascal Triangle."""
    lucas_pascal_triangle = LucasPascalTriangle(5)
    expected = [
        [1],
        [3, 3],
        [4, 6, 4],
        [7, 10, 10, 7],
        [11, 17, 20, 17, 11]
    ]
    assert lucas_pascal_triangle.triangle == expected


def test_wythoff_triangle():
    """Tests for Wythoff Triangle."""
    wythoff_triangle = WythoffTriangle(5)
    expected = [
        [1],
        [4, 2],
        [6, 7, 3],
        [9, 10, 11, 5],
        [12, 15, 16, 18, 8]
    ]
    assert wythoff_triangle.triangle == expected
