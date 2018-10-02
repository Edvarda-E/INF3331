import pytest
import numpy as np
import mandelbrot_package
compute_mandelbrot = mandelbrot_package.compute_mandelbrot


def test_region_outside_of_mandelbrot():
    """
    Test that verifies whether all values in the matrix are 0, meaning the set it entirely outside of the mandelbrot
    set
    """
    mandelbrot_matrix = compute_mandelbrot(3, 4, 3, 4, 100, 100)
    assert np.all(mandelbrot_matrix == 0)

    mandelbrot_matrix = compute_mandelbrot(-5, -7, -4, -3, 200, 200)
    assert np.all(mandelbrot_matrix == 0)


def test_region_inside_of_mandelbrot():
    """
    Test that verifies whether all values in the matrix are 1000, meaning the set it entirely inside the mandelbrot
    set
    """
    mandelbrot_matrix = compute_mandelbrot(0.0001, 0.0001, -0.0001, -0.00001, 200, 200)
    assert np.all(mandelbrot_matrix == 1000)

    mandelbrot_matrix = compute_mandelbrot(0.0003, 0.0002, 0.0007, 0.00013, 200, 200)
    assert np.all(mandelbrot_matrix == 1000)
