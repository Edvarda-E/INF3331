import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(z, max_iterations=1000):
    """
    Function that returns either how many steps it took before the value of the quadratic polynomial x^2+c exceeds
    2, or returns the max_iterations number, defaults to 1000

    Arguments:
        z (complex number): Seed for the iteration, start value for c
        max_iterations (int, optional): How many times the function should loop before it exits. Defaults to 1000

    Returns:
        int < max_iterations:  How many steps it took for the value of the quadratic polynomial to exceed 2
        int == max_iterations: Seed is presumably in Mandelbrot Set
    """
    c = z
    for i in range(max_iterations):
        # print(z)
        if abs(z) > 2:
            return i
        z = z * z + c
    return max_iterations


def draw_mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iterations):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    temp_matrix = np.empty((len(r1), len(r2)))
    for i in range(len(r1)):
        for j in range(len(r2)):
            real = r1[i]
            imag = r2[j]
            temp_matrix[i, j] = mandelbrot(complex(real, imag), max_iterations)
    return temp_matrix


plt.imshow(draw_mandelbrot_set(-0.74877, -0.74872, 0.06505, 0.06510, 1000, 1000, 1000))
plt.show()
