# Assignment 4
This is the directory for assignment 4, done by Edvarda Eriksen (ererikse).

## General notice
A lot of the code in this assignment will be repeated, rather than creating general
files. This includes the "main" function 
```
if __name__ == "__main__":
    mandelbrot_fast_parameters = [-2.0, 0.5, -1.25, 1.25, 1000, 1000, 80]
    mandelbrot_slow_parameters = [-0.74877, -0.74872, 0.06505, 0.06510, 1000, 1000, 1000]
    main(*mandelbrot_fast_parameters)
    # main(*mandelbrot_slow_parameters)
```
This is where you can easily modify the parameters of the implementation, and can be found at the bottom of 
`mandelbrot_1.py`, `mandelbrot_2.py` and `mandelbrot_3.py`.

Alternatively you can run the user interface created in Assignment 4.5 (see below), where you can input your own 
parameters by calling the script directly with your desired implementation. 

*Potential warnings*: 
* `#!/usr/bin/env python` was not included in the python files as I used the built-in python3 interpreter in PyCharm
* Last commit was pushed fairly late, so if the snapshots are taken manually there might be a mistake
## 4.1 - Python implementation of Mandelbrot Set
Running the script
```
$ python mandelbrot_1.py
```

**Additional decisions**
* Everytime you run the script, you store an image called `python_image`, unless specifically specified otherwise in 
task 4.5.
* This image will be overwritten everytime the script is re-run

## 4.2 - Numpy implementation of Mandelbrot Set
Running the script
```
$ python mandelbrot_2.py
```

**Additional decisions**
* Everytime you run the script, you store an image called `numpy_image`, unless specifically specified otherwise in 
task 4.5.
* If an image exists with the same name, it will be overwritten everytime the script is re-run

## 4.3 - Numba implementation of Mandelbrot Set
Running the script
```
$ python mandelbrot_3.py
```

**Additional decisions**
* Everytime you run the script, you store an image called `numba_image`, unless specifically specified otherwise in 
task 4.5.
* If an image exists with the same name, it will be overwritten everytime the script is re-run

## 4.4 - Cython implementation of Mandelbrot Set
Requirements:
```
Python v3
Cython v0.28.6
Visual Studio C++ Build Tools 2015 or something similar
```
I used pip to install cython, and ran cython through the Visual Studio C++ Build Tools compiler.
Failure to have a correct C compiler will result in `error: Unable to find vcvarsall.bat`

Running the script
```
$ python cython_setup.py build_ext --inplace
$ python mandelbrot_4.py
```

**Additional decisions**
* Everytime you run the script, you store an image called `cython_image`, unless specifically specified otherwise in 
task 4.5.
* If an image exists with the same name, it will be overwritten everytime the script is re-run

## 4.5 - User interface
For help on how to use the interface, please run 
```
$ python mandelbrot.py --help
```
Here you will get information on what the script expects, and how to run it.

An example run is: 
```
$  python mandelbrot.py -0.74877 -0.74872 0.06505 0.06510 1000 1000 my_cython_img cython
```

## 4.6 Packaging and unit tests
As seen in the lecture notes, to store the package and run the setup.py, run
```
$ pip install . --user
```

After this is done you can import the package `mandelbrot_package` like any other python package and call
`mandelbrot_package.compute_mandelbrot` like normal.

Implemented all tests using plain pytest. To run the tests go to this directory and run 
```
pytest
```
or 
```
pytest -v
```

If all tests succeed it will say "n tests passed in x seconds", as a part of pytest