import pytest
from process_data import *


@pytest.fixture
def x():
    x = [0, 1, 4, 9]
    return [float(n) for n in x]


def test_derivative_values(x):
    assert derivative(x) == [1, 3, 5]
    assert derivative(derivative(x)) == [2, 2]


def test_derivative_len(x):
    assert len(derivative(x)) == len(x) - 1


def test_derivative_error():
    int_3d = [[[0], [1], [4], [9]]]
    with pytest.raises(ValueError):
        process_data(int_3d)


def test_find_max_idx(x):
    y = [1, 1, 1, 1]
    assert find_max_idx(x) == 3
    assert find_max_idx(y) == 0, "failure when max value occurs more than once"


def test_find_derivatives_maxima(x):
    # xp_max is 5 and xpp_max is 2 (respective true indices are 2 and 0)
    # indices are padded with +n and +(n+1) for human interpretation
    assert find_derivatives_maxima(x) == [3, 2], "check if cycle increment `n` is accounted for correctly"
