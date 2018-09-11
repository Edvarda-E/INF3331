#!/usr/bin/env python
import math


class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Assignment 3.3

    def conjugate(self):
        self.imag = abs(self.imag) if self.imag < 0 else -self.imag
        return str(self)

    def modulus(self):
        a = self.real**2
        b = self.imag**2
        return math.sqrt(a + b)

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, int):
            return Complex(self.real + other, self.imag)
        else:
            print("Can't add input")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, int):
            return Complex(self.real - other, self.imag)
        else:
            print("Can't subtract input")

    def __mul__(self, other):
        if isinstance(other, Complex):
            a = self.real
            b = self.imag
            c = other.real
            d = other.imag

            real = (a*c) - (b*d)
            imag = (a*d) + (b*c)
            return Complex(real, imag)
        else:
            "Cannot multiply other than Complex cases"

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.real == other.real and self.imag == other.imag
        else:
            return False

    # Assignment 3.4
    def __radd__(self, other):
        pass

    def __rmul__(self, other):
        pass

    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        pass

    def __repr__(self):
        plus_minus = "+" if self.imag > 0 else "-"
        if self.real != 0 and self.imag != 0:
            if self.imag == 1 or self.imag == -1:
                return "%s %s i" % (str(self.real), plus_minus)
            else:
                return "%s %s %si" % (str(self.real), plus_minus, str(abs(self.imag)))
        elif self.real == 0 and self.imag != 0:
            if self.imag == 1:
                return "i"
            elif self.imag == -1:
                return "%si" % plus_minus
            else:
                return "%si" % str(self.imag)
        elif self.real == 0 and self.imag == 0:
            return "0"
        else:
            return "%s" % self.real
