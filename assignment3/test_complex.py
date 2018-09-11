#!/usr/bin/env python
from complex import Complex


def test_addition():
    z = Complex(0, 0)
    w = Complex(0, 0)
    assert (z + w) == "0"

    assert (z + 1) == "1"

    z = Complex(0, 1)
    w = Complex(0, -2)
    assert (z + w) == "i"

    z = Complex(0, -2)
    w = Complex(0, 1)
    assert (z + w) == "-i"

    z = Complex(0, 2)
    w = Complex(0, 3)
    assert (z + w) == "5i"

    z = Complex(0, -7)
    w = Complex(0, -3)
    assert (z + w) == "-10i"

    z = Complex(3, 0)
    w = Complex(7, 0)
    assert (z + w) == "10"

    z = Complex(-12, 0)
    w = Complex(6, 0)
    assert (z + w) == "-6"

    z = Complex(1, 2)
    w = Complex(3, 1)
    assert (z + w) == "4 + 3i"

    z = Complex(3, 0)
    w = Complex(9, 1)
    assert (z + w) == "12 + i"

    z = Complex(9, -2)
    w = Complex(8, -3)
    assert (z + w) == "17 - 5i"

    z = Complex(6, -3)
    w = Complex(7, 2)
    assert (z + w) == "13 - i"

    z = Complex(-6, 0)
    w = Complex(-8, 1)
    assert (z + w) == "-14 + i"

    z = Complex(-3, 3)
    w = Complex(-1, 8)
    assert (z + w) == "-4 + 8i"

    z = Complex(-1, -5)
    w = Complex(-8, -3)
    assert (z + w) == "-9 - 8i"

    z = Complex(-11, -2)
    w = Complex(-15, 1)
    assert (z + w) == "-26 - i"


def test_radd_addition():
    pass


def test_subtraction():
    z = Complex(0, 0)
    w = Complex(0, 0)
    assert (z - w) == "0"

    assert (z - 1) == "-1"

    z = Complex(0, 2)
    w = Complex(0, 1)
    assert (z - w) == "i"

    z = Complex(0, -2)
    w = Complex(0, -1)
    assert (z - w) == "-i"

    z = Complex(0, 8)
    w = Complex(0, 4)
    assert (z - w) == "4i"

    z = Complex(0, -7)
    w = Complex(0, -3)
    assert (z - w) == "-4i"

    z = Complex(17, 0)
    w = Complex(12, 0)
    assert (z - w) == "5"

    z = Complex(-12, 0)
    w = Complex(6, 0)
    assert (z - w) == "-18"

    z = Complex(4, 7)
    w = Complex(2, 3)
    assert (z - w) == "2 + 4i"

    z = Complex(13, 1)
    w = Complex(9, 0)
    assert (z - w) == "4 + i"

    z = Complex(9, -2)
    w = Complex(8, 4)
    assert (z - w) == "1 - 6i"

    z = Complex(6, 3)
    w = Complex(-7, 4)
    assert (z - w) == "13 - i"

    z = Complex(-10, 1)
    w = Complex(-8, 0)
    assert (z - w) == "-2 + i"

    z = Complex(-3, 7)
    w = Complex(-1, 4)
    assert (z - w) == "-2 + 3i"

    z = Complex(-17, -5)
    w = Complex(8, 3)
    assert (z - w) == "-9 - 8i"

    z = Complex(-11, 2)
    w = Complex(15, 3)
    assert (z - w) == "-26 - i"


def test_rsub_subtraction():
    pass


def test_modulus():
    pass


def test_conjugate():
    pass

# TODO: (Optional) Test multiplication
