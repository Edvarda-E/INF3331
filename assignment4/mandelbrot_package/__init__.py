from numba import jit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


@jit
def mandelbrot(z, max_iterations):
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


def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None):
    """
    Function that takes a range of values and calculates the mandelbrot set, then returns the values as a matrix

    Arguments:
        xmin (float): Lowest value for x, the real part of the complex number
        xmax (float): Highest value for x, the real part of the complex number
        ymin (float): Lowest value for y, the imaginary part of the complex number
        ymax (float): Highest value for y, the imaginary part of the complex number
        Nx (int): The width of the matrix
        Ny (int): The height of the matrix
        max_escape_time (int, optional): Number of times the mandelbrot function should iterate. Defaults to 1000
        plot_filename(str, optional: Name of output file to be stored, if desirable. Defaults to None

    Returns:
        matrix (numpy 2d array): Results of all the calculations done
    """
    # This would have been iteration number 0, e.g. the first numbers to be tested
    # I found this more efficient than calculating all values of the mandelbrot set first
    if abs(xmin + 1j*ymin) > 2.0:
        return np.zeros((Nx, Ny))

    row = np.linspace(xmin, xmax, Nx)
    col = np.linspace(ymin, ymax, Ny)
    temp_matrix = np.empty((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            temp_matrix[i, j] = mandelbrot(row[i] + 1j * col[j], max_escape_time)

    if plot_filename is not None:
        colours = [(0.1411764705882353, 0.1607843137254902, 0.1803921568627451),  # grey - rgb(36, 41, 46)
                   (0.11372549019607843, 0.7254901960784313, 0.32941176470588235)]  # green - rgb(29, 185, 84)
        custom_colourmap = LinearSegmentedColormap.from_list("gray_to_green", colours, 1000)
        extent = [xmin, xmax, ymin, ymax]
        plt.imshow(temp_matrix, cmap=custom_colourmap, extent=extent)
        plt.savefig(plot_filename + ".png")

    return temp_matrix
