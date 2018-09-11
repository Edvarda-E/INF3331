#!/usr/bin/env python
import math


class Complex:

    def __init__(self, real, imag):
        """Form a complex number.

        Arguments:
            real: The real part of the complex number
            imag: The imaginary part of the complex number
        """
        self.real = real
        self.imag = imag

    # Assignment 3.3

    def conjugate(self):
        """ Conjugates a complex number, changing the sign of the
        imaginary part of the number

        Arguments:
            self: A Complex number - Complex(a, b)

        Return:
            Complex(a, -b) if b was initially positive
            Complex(a, b) if b was initially negative
        """
        imag = abs(self.imag) if self.imag < 0 else -self.imag
        return Complex(self.real, imag)

    def modulus(self):
        """ Calculate the modulus of a complex number

        Arguments:
            self: A Complex number - Complex(a, b)

        Return
            Square root of the real part to the power of two,
            plus the imaginary part to the power of two
        """
        a = self.real**2
        b = self.imag**2
        return math.sqrt(a + b)

    def __add__(self, other):
        """ Calculate the addition of a complex number and some other number

        Arguments:
            self: A Complex number - Complex(a, b)
            other: Can be a complex number, an int or a float

        Return
            Complex(self.real + other.real, self.imag + other.imag)
        """
        if isinstance(other, Complex) or isinstance(other, complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, int):
            return Complex(self.real + other, self.imag)
        else:
            print("Can't add input")

    def __sub__(self, other):
        """ Calculates the subtraction of a complex number and some other number

        Arguments
            self: A Complex number - Complex(a, b)
            other: Can be a complex number, an int or a float

        Return
            Complex(self.real - other.real, self.imag - other.imag)
        """
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, int):
            return Complex(self.real - other, self.imag)
        else:
            print("Can't subtract input")

    def __mul__(self, other):
        """ Calculates the subtraction of a complex number and some other number

        Arguments
            self: A Complex number - Complex(a, b)
            other: Can be a complex number, an int or a float

        Return
            Complex(ac - bd, ad + bc)
        """
        a = self.real
        b = self.imag
        c = other.real
        d = other.imag

        real = (a*c) - (b*d)
        imag = (a*d) + (b*c)
        return Complex(real, imag)

    def __eq__(self, other):
        """ Verifies if two complex numbers are equal or not

        Arguments
            self: A Complex number - Complex(a, b)
            other: Can be a complex number, an int or a float

        Return
            Complex(self.real - other.real, self.imag - other.imag)
        """
        if isinstance(other, Complex) or isinstance(other, complex):
            return self.real == other.real and self.imag == other.imag
        else:
            return False

    # Assignment 3.4
    def __radd__(self, other):
        """ Enables a non-complex number to be added to a complex number"""
        return self + other

    def __rsub__(self, other):
        """ Enables a non-complex number to be subtracted to a complex number"""
        return -self + other

    def __rmul__(self, other):
        """ Enables a non-complex number to be multiplied by a complex number"""
        return self * other

    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        return Complex(-self.real, -self.imag)

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        return self.real + self.imag * 1j

    def __str__(self):
        """ A string function that converts the complex number to a readable string.
        Will write all numbers on the form a+bi
        """
        # Saves the sign to ensure the space between the sign and
        # the imaginary part , e.g 1 + 2i
        plus_minus = "+" if self.imag > 0 else "-"

        if self.real != 0 and self.imag != 0:
            # Special case where output is either +i or -i, not +1i or -1i
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
