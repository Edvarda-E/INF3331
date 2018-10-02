import argparse
import mandelbrot_1
import mandelbrot_2
import mandelbrot_3
import mandelbrot_4
save_python_implementation = mandelbrot_1.main
save_numpy_implementation = mandelbrot_2.main
save_numba_implementation = mandelbrot_3.main
save_cython_implementation = mandelbrot_4.main

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
parser.add_argument("width",
                    type=int,
                    help="the width resolution in pixels")
parser.add_argument("height",
                    type=int,
                    help="the height resolution in pixels")
parser.add_argument("img_filename",
                    type=str,
                    help="name of output image file, excluding the file format. The format will be .png")
parser.add_argument("implementation",
                    type=str,
                    choices=["python", "numpy", "numba", "cython"],
                    help="which of the implementations to be used")
args = parser.parse_args()

if args.implementation == "python":
    save_python_implementation(args.xmin, args.xmax, args.ymin, args.ymax, args.width, args.height, args.img_filename)
elif args.implementation == "numpy":
    save_numpy_implementation(args.xmin, args.xmax, args.ymin, args.ymax, args.width, args.height, args.img_filename)
elif args.implementation == "numba":
    save_numba_implementation(args.xmin, args.xmax, args.ymin, args.ymax, args.width, args.height, args.img_filename)
else:
    # argparse will crash the program if the choice isn't valid, hence no need to check if the last is cython
    save_cython_implementation(args.xmin, args.xmax, args.ymin, args.ymax, args.width, args.height, args.img_filename)
