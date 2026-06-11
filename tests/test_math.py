from playground.math import divide, multiply


def test_divide_zero_by_five_is_zero():
    assert divide(0, 5) == 0


def test_multiply_two_positive_integers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero_is_zero():
    assert multiply(7, 0) == 0


def test_multiply_negative_and_positive():
    assert multiply(-3, 5) == -15


def test_multiply_two_negatives_is_positive():
    assert multiply(-2, -6) == 12


def test_multiply_floats():
    assert multiply(2.5, 4) == 10.0
