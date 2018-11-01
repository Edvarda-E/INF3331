# Assignment 5
This is the directory for Assignment 5, done by Edvarda Eriksen (ererikse) enrolled in INF4331.

## General notice
This repository is on a 3-day extension period due to sickness and is not done yet!

This assignment was solved on a Ubuntu 18.04 system, and has been tested on a Windows 10 WLS system.
## 5.1
Running the script
```
$ python3 highlighter.py test.syntax test.theme
```


## 5.2 - Colortheme for Python
Running the demo:
```
$ python3 highlighter.py python.syntax python.theme

$ python3 highlighter.py python.syntax python2.theme
```

### while-loops
```
Full RegEx: (\bwhile\b\h*)(?:\(\h*)?(?:\w+\h*|\w+\h*(?:==|!=|<>|>|<|>=|<=)\h*\w+)(?:\h*\))?(?::)

(\bwhile\b\h*)              # while key-word with trailing optional horizontal whitespace
(?:\(\h*)?                  # Optional ( and horizontal whitespace before expression

(?:\w+\h*                   # Matches a standalone expression, e.g. a parameter "while i"
|                           # Or
\w+\h*                      # Matches a plain expresison and optional whitespace ...
    (?:==|!=|<>|>|<|>=|<=)  # Followed by one of these comparators ...
\h*\w+)                     # Followed by optional whitespace and another expression

(?:\h*\))?                  # Optional whitespace and closing )
(?::)                       # Ended by the needed :
```
All groups after the while-keyword is non-captured as I do not wish to color them, only match them.

*Known problems and additional decisions for while*:
- The RegEx wrongfully matches statements like `while (i>2:`
- The while RegEx does not cover and/or operators, e.g. `while (i>2) and (j<3):`
- The while RegEx does not cover mathematical operators, e.g. `while(i % 2):`


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