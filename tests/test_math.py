import pytest

from playground.math import divide


def test_divide_zero_by_five_is_zero():
    assert divide(0, 5) == 0


def test_divide_six_by_two_is_three():
    assert divide(6, 2) == 3


def test_divide_returns_true_division_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
