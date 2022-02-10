"""
Test API Calls
--------------

Verify that API calls meet requirements.
"""

from calculator.calculation import Basic, DivideByZero, NotEnoughNumbers

import pytest


def test_add():
    """Verify that add works."""
    basic = Basic()

    assert basic.add(1, 2) == 3
    assert basic.add(1, 2, 3) == 6

    with pytest.raises(NotEnoughNumbers):
        basic.add(1)


def test_subtract():
    """Verify that subtract works."""
    basic = Basic()

    assert basic.sub(10, 3) == 7
    assert basic.sub(10, 3, 2) == 5

    with pytest.raises(NotEnoughNumbers):
        basic.sub(10)


def test_multiply():
    """Verify that multiplication works."""
    basic = Basic()

    assert basic.mul(5, 4) == 20
    assert basic.mul(3, 2, -1) == -6

    with pytest.raises(NotEnoughNumbers):
        basic.mul(99)


def test_division():
    """Verify that division works."""
    basic = Basic()

    assert basic.div(10, 5) == 2
    assert basic.div(17, 2) == 8.5

    with pytest.raises(NotEnoughNumbers):
        basic.div(1)

    with pytest.raises(DivideByZero):
        basic.div(9, 0)
