import cython
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

cdef int mandelbrot(double input_real, double input_imag, int max_iterations):
    cdef:
        double complex z = input_real+input_imag*1j
        double complex c = z
        int i

    for i in range(max_iterations):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iterations

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing
cpdef mandelbrot_set(double xmin, double xmax, double ymin, double ymax, int width, int height, int max_iterations,
                     image_name="test"):
    cdef:
        double[:] row = np.linspace(xmin, xmax, width)
        double[:] col = np.linspace(ymin, ymax, height)
        int[:,:] mandelbrot_matrix = np.empty((width,height), np.int)
        int i,j

    for i in range(width):
        for j in range(height):
            mandelbrot_matrix[i,j] = mandelbrot(row[i], col[j], max_iterations)

    colours = [(0.1411764705882353, 0.1607843137254902, 0.1803921568627451),  # grey - rgb(36, 41, 46)
               (0.11372549019607843, 0.7254901960784313, 0.32941176470588235)]  # green - rgb(29, 185, 84)
    custom_colourmap = LinearSegmentedColormap.from_list("gray_to_green", colours, 1000)
    plt.imshow(mandelbrot_matrix, cmap=custom_colourmap, extent=[xmin, xmax, ymin, ymax])
    plt.savefig(image_name + ".png")