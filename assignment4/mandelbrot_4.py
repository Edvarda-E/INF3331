from mandelbrot_cython import mandelbrot_set
from datetime import datetime


def main(xmin, xmax, ymin, ymax, width, height, image_name, max_iterations=1000):
    mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iterations, image_name)


# Runs if mandelbrot_1.py is called directly from commandline
if __name__ == "__main__":
    startTime = datetime.now()
    print("Program started")
    main(-2.0, 0.5, -1.25, 1.25, 1000, 1000, "cython_image", 80)
    # main(-0.74877, -0.74872, 0.06505, 0.06510, 1000, 1000, "cython_image", 1000)
    print(datetime.now() - startTime)
