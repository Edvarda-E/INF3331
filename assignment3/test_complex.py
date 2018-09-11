#!/usr/bin/env python
import pytest
import math
from complex import Complex


def test_addition():
    """
    Verifies that the __add__ magic function works as intended
    """
    z = Complex(0, 0)
    w = Complex(0, 0)
    assert (z + w) == Complex(0, 0)     # "0"

    assert (z + 1) == Complex(1, 0)     # "1"

    z = Complex(0, 1)
    w = Complex(0, 0)
    assert (z + w) == Complex(0, 1)     # "i"

    z = Complex(0, -2)
    w = Complex(0, 1)
    assert (z + w) == Complex(0, -1)    # "-i"

    z = Complex(0, 2)
    w = Complex(0, 3)
    assert (z + w) == Complex(0, 5)     # 5

    z = Complex(0, -7)
    w = Complex(0, -3)
    assert (z + w) == Complex(0, -10)   # "-10i"

    z = Complex(3, 0)
    w = Complex(7, 0)
    assert (z + w) == Complex(10, 0)    # "10"

    z = Complex(-12, 0)
    w = Complex(6, 0)
    assert (z + w) == Complex(-6, 0)    # "-6"

    z = Complex(1, 2)
    w = Complex(3, 1)
    assert (z + w) == Complex(4, 3)      # "4 + 3i"

    z = Complex(3, 0)
    w = Complex(9, 1)
    assert (z + w) == Complex(12, 1)    # "12 + i"

    z = Complex(9, -2)
    w = Complex(8, -3)
    assert (z + w) == Complex(17, -5)   # "17 - 5i"

    z = Complex(6, -3)
    w = Complex(7, 2)
    assert (z + w) == Complex(13, -1)   # "13 - i"

    z = Complex(-6, 0)
    w = Complex(-8, 1)
    assert (z + w) == Complex(-14, 1)   # "-14 + i"

    z = Complex(-3, 3)
    w = Complex(-1, 8)
    assert (z + w) == Complex(-4, 11)   # "-4 + 11i"

    z = Complex(-1, -5)
    w = Complex(-8, -3)
    assert (z + w) == Complex(-9, -8)   # "-9 - 8i"

    z = Complex(-11, -2)
    w = Complex(-15, 1)
    assert (z + w) == Complex(-26, -1)   # "-26 - i"


def test_radd_addition():
    """ Verifies that the __radd__ magic function works as intended """
    assert 2 + Complex(3, 7) == Complex(5, 7)
    assert (2+2j) + Complex(2, 3) == Complex(4, 5)
    assert (-4+1j) + Complex(2, 5) == Complex(-2, 6)


def test_subtraction():
    """ Verifies that the __sub__ magic function works as intended """

    z = Complex(0, 0)
    w = Complex(0, 0)
    assert (z - w) == Complex(0, 0)     # "0"

    assert (z - 1) == Complex(-1, 0)    # "-1"

    z = Complex(0, 2)
    w = Complex(0, 1)
    assert (z - w) == Complex(0, 1)     # "i"

    z = Complex(0, -2)
    w = Complex(0, -1)
    assert (z - w) == Complex(0, -1)    # "-i"

    z = Complex(0, 8)
    w = Complex(0, 4)
    assert (z - w) == Complex(0, 4)     # "4i"

    z = Complex(0, -7)
    w = Complex(0, -3)
    assert (z - w) == Complex(0, -4)    # "-4i"

    z = Complex(17, 0)
    w = Complex(12, 0)
    assert (z - w) == Complex(5, 0)     # "5"

    z = Complex(-12, 0)
    w = Complex(6, 0)
    assert (z - w) == Complex(-18, 0)   # "-18"

    z = Complex(4, 7)
    w = Complex(2, 3)
    assert (z - w) == Complex(2, 4)     # "2 + 4i"

    z = Complex(13, 1)
    w = Complex(9, 0)
    assert (z - w) == Complex(4, 1)     # "4 + i"

    z = Complex(9, -2)
    w = Complex(8, 4)
    assert (z - w) == Complex(1, -6)    # "1 - 6i"

    z = Complex(6, 3)
    w = Complex(-7, 4)
    assert (z - w) == Complex(13, -1)   # "13 - i"

    z = Complex(-10, 1)
    w = Complex(-8, 0)
    assert (z - w) == Complex(-2, 1)    # "-2 + i"

    z = Complex(-3, 7)
    w = Complex(-1, 4)
    assert (z - w) == Complex(-2, 3)    # "-2 + 3i"

    z = Complex(-17, -5)
    w = Complex(8, 3)
    assert (z - w) == Complex(-25, -8)  # "-25 - 8i"

    z = Complex(-11, 2)
    w = Complex(15, 3)
    assert (z - w) == Complex(-26, -1)  # "-26 - i"


def test_rsub_subtraction():
    """ Verifies that the __rsub__ magic function works as intended """
    assert 3 - Complex(3, 3) == Complex(0, -3)
    assert (-4+9j) - Complex(-3, -4) == Complex(-1, 13)
    assert (12+6j) - Complex(4, 3) == Complex(8, 3)


def test_modulus():
    """ Verifies that the modulus function works as intended """
    z = Complex(0, 0)
    assert z.modulus() == 0

    z = Complex(3, 7)
    assert z.modulus() == math.sqrt(58)

    z = Complex(-6, -4)
    assert z.modulus() == 2*math.sqrt(13)

    z = Complex(-10, 0)
    assert z.modulus() == 10

    z = Complex(-2, -8)
    assert z.modulus() == 2*math.sqrt(17)


def test_conjugate():
    """ Verifies that the conjugate function works as intended """
    z = Complex(0, 0)
    assert z.conjugate() == Complex(0, 0)       # "0"

    z = Complex(4, 0)
    assert z.conjugate() == Complex(4, 0)       # "4"

    z = Complex(0, 11)
    assert z.conjugate() == Complex(0, -11)     # "-11i"

    z = Complex(3, 7)
    assert z.conjugate() == Complex(3, -7)      # "3 - 7i"

    z = Complex(-9, -4)
    assert z.conjugate() == Complex(-9, 4)      # "-9 + 4i"

    z = Complex(12, -9)
    assert z.conjugate() == Complex(12, 9)      # "12 + 9i"

    z = Complex(-3, 7)
    assert z.conjugate() == Complex(-3, -7)     # "-3 - 7i"


def test_equals():
    """ Verifies that the __eq__ magic function works as intended """
    z = Complex(0, 0)
    assert z == Complex(0, 0)

    z = Complex(2, 3)
    assert z == Complex(2, 3)

    z = Complex(-2, -3)
    assert z == Complex(-2, -3)

    z = Complex(-19, 20)
    assert z == Complex(-19, 20)

    z = Complex(13, -37)
    assert z == Complex(13, -37)


def test_multiplication():
    """ Verifies that the __mul__ magic function works as intended """
    z = Complex(0, 0)
    w = Complex(0, 0)
    assert (z * w) == Complex(0, 0)     # "0"

    z = Complex(1, 1)
    w = Complex(1, 1)
    assert (z * w) == Complex(0, 2)     # "2i"

    z = Complex(-8, -2)
    w = Complex(3, 9)
    assert (z * w) == Complex(-6, -78)  # "-6 - 78i"

    z = Complex(4, 1)
    w = Complex(7, -3)
    assert (z * w) == Complex(31, -5)   # "31 - 5i"

    z = Complex(1, 4)
    w = Complex(5, 1)
    assert (z * w) == Complex(1, 21)    # "1 + 21i"


def test_rmul_multiplication():
    """ Verifies that the __rmul__ magic function works as intended """
    assert 16 * Complex(4, 1) == Complex(64, 16)
    assert 4 * Complex(3, 4) - 2 == Complex(10, 16)
