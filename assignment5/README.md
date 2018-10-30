# Assignment 5
This is the directory for assignment 5, done by Edvarda Eriksen (ererikse) enrolled in INF4331.

## General notice
This repository is on a 3-day extension period due to sickness and is not done yet!
## 5.1
Running the script
```
$ python3 highlighter.py test.syntax test.theme
```


## 5.2 
Running the script
```
$ python mandelbrot_2.py
```

**Additional decisions**
* Everytime you run the script, you store an image called `numpy_image`, unless specifically specified otherwise in 
task 4.5.
* If an image exists with the same name, it will be overwritten everytime the script is re-run

## 5.3
Not done

## 5.4
```
$ python3 grep.py test3.txt test.syntax
```
or
```
$ python3 grep.py test3.txt test.syntax --highlighter
```

## 5.5
```
$ python3 diff.py text1.txt text2.txt
```

## 5.6 
Again, as the last task was solved in the terminal, this is also solved slightly differently as follows:
```
$ python3 diff_demo.py b.txt diff.syntax diff.theme
```
Here I also decided to handle the lines as the regexes proceeded, and not vice versa, hence first you are presented
all the additions, then the deletions, then the unchanged lines.