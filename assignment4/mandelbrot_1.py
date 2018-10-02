import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime


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
        if abs(z) > 2:
            return i
        z = z * z + c
    return max_iterations


def draw_mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iterations):
    """
    Function that generates a matrix, feeding x and y to the mandelbrot function as a complex number x + yj, and stores
    the return values for each coordinate

    Arguments:
        xmin (float): Lowest value for x, the real part of the complex number
        xmax (float): Highest value for x, the real part of the complex number
        ymin (float): Lowest value for y, the imaginary part of the complex number
        ymax (float): Highest value for y, the imaginary part of the complex number
        width (int): The width of the matrix
        height (int): The height of the matrix
        max_iterations (int): Number of times the mandelbrot function should iterate

    Returns:
        temp_matrix (2d Array): The result of the calculations for each complex number x + yj
    """
    row = np.linspace(xmin, xmax, width)
    col = np.linspace(ymin, ymax, height)
    temp_matrix = np.empty((len(row), len(col)))
    for i in range(len(row)):
        for j in range(len(col)):
            real = row[i]
            imag = col[j]
            temp_matrix[i, j] = mandelbrot(complex(real, imag), max_iterations)
    return temp_matrix


def main(xmin, xmax, ymin, ymax, width, height, image_name="python_image", max_iterations=1000):
    """
    The function that generates a colourmap, calculates the mandelbrot set with draw_mandelbrot_set and stores the
    result as an image
    """

    startTime = datetime.now()
    print("Program started")

    # rgb values are divided by 255 to become values between 0 and 1
    colours = [(0.1411764705882353, 0.1607843137254902, 0.1803921568627451),    # grey - rgb(36, 41, 46)
               (0.11372549019607843, 0.7254901960784313, 0.32941176470588235)]  # green - rgb(29, 185, 84)
    custom_colourmap = LinearSegmentedColormap.from_list("gray_to_green", colours, 1000)
    mandelbrot_matrix = draw_mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iterations)
    extent = [xmin, xmax, ymin, ymax]

    plt.imshow(mandelbrot_matrix, cmap=custom_colourmap, extent=extent)
    plt.savefig(image_name + ".png")
    print(datetime.now() - startTime)


# Runs if mandelbrot_1.py is called directly from commandline
if __name__ == "__main__":
    mandelbrot_fast_parameters = [-2.0, 0.5, -1.25, 1.25, 1000, 1000, "python_image",  80]
    mandelbrot_slow_parameters = [-0.74877, -0.74872, 0.06505, 0.06510, 1000, 1000, "python_image", 1000]
    # main(*mandelbrot_fast_parameters)
    main(*mandelbrot_slow_parameters)

