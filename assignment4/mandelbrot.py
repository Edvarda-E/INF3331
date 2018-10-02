import argparse


parser = argparse.ArgumentParser(description="Calculate the mandelbrot set and save the output image created by one of"
                                             " three implementations")
parser.add_argument("xmin",
                    type=float,
                    help="lowest value for x, the real part of the complex number")
parser.add_argument("xmax",
                    type=float,
                    help="highest value for x, the real part of the complex number")
parser.add_argument("ymin",
                    type=float,
                    help="lowest value for y, the imaginary part of the complex number")
parser.add_argument("ymax",
                    type=float,
                    help="highest value for y, the imaginary part of the complex number")
parser.add_argument("img_filename",
                    type=str,
                    help="name of output image file, excluding the file format")
parser.add_argument("implementation",
                    type=str,
                    choices=["python", "numpy", "numba", "cython"],
                    help="which of the implementations to be used")
args = parser.parse_args()

if args.implementation == "python":
    print("python")
elif args.implementation == "numpy":
    print("numpy")
elif args.implementation == "numba":
    print("numba")
else:
    # argparse will crash the program if the choice isn't valid
    print("cython")
