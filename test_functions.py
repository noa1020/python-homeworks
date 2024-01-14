import pytest
import functions


@pytest.mark.parametrize("n, expected", [
    (10, [2, 3, 5, 7]),
    (1, []),
    (-10, []),
    (0, [])])
def test_find_primes(n, expected):
    assert functions.find_primes(n) == expected


@pytest.mark.parametrize("char_list, expected", [
    (['c', 'a', 'b'], ['a', 'b', 'c']),
    ([], []),
    (['b', 'a', 'b', 'c', 'a'], ['a', 'a', 'b', 'b', 'c']),
    (['x'], ['x']),
    (['Z', 'a', 'B', 'c'], ['B', 'Z', 'a', 'c']),
    (['1', '2', '3'], ['1', '2', '3']),
    ([3, 1, 2], [1, 2, 3]),
    (['x'] * 1000, ['x'] * 1000),
])
def test_sort_list(char_list, expected):
    assert functions.sort_list(char_list) == expected


@pytest.mark.parametrize("n, expected", [
    ("2+2", 4), ("(4+5)*2", 18), ("2+*2", None), ("", None)])
def test_calculate_expression(n, expected):
    assert functions.calculate_expression(n) == expected
