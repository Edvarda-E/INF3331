# Assignment 3
This is the directory for assignment 3, done by Edvarda Eriksen (ererikse).

## 3.1 - Wordcount
Running the script
```
$ chmod a+x wc.py
$ ./wc.py ./example.txt
```

**Additional decisions**
* I decided to include `\n` in the character count, resulting in more characters than "conventional" character trackers.
* Empty lines at the end of a file does not count

## 3.2 - Unit tests for complex numbers
Implemented all tests using plain pytest. To run the tests go to this directory and run 
```
pytest
```
or 
```
pytest -v
```

If all tests succeed it will say "n tests passed in x seconds", as a part of pytest

## 3.3 - Implement complex numbers
Implemented all needed functions, in a non manipulative fashion (meaning the object is not changed)

## 3.4 - Make your implementation work with Python’s complex numbers
Code now also supports "normal" Python complex numbers
