def mandelbrot(z, max_iterations=1000):
    """
    Function that returns either how many steps it took before the value of the quadratic polynomial x^2+c exceeds
    2, or returns the maxIteration number, defaults to 1000

    Arguments:
        z (complex number): Seed for the iteration
        max_iterations (int, optional): How many times the function should loop before it exits. Defaults to 1000

    Returns:
        int < maxIterations:  Value of quadratic polynomial exceeded 2 after this many steps
        int == maxIterations: Seed is probably in Mandelbrot Set
    """
    c = z
    for i in range(max_iterations):
        print(z)
        if abs(z) > 2:
            return i
        z = z*z + c
    return max_iterations


print(mandelbrot(-0.52+0.57j))
