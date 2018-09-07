#!/usr/bin/env python
import sys
import os


def count_and_print(file):
    fileName = os.path.basename(file)
    file = open(file, 'r')
    lineCount = 0
    wordCount = 0
    charCount = 0

    for line in file.readlines():
        lineCount += 1
        # print(len(line))
        charCount += len(line)
        for word in line.split():
            wordCount += 1
    file.close()
    print(lineCount, wordCount, charCount, fileName)


if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
    count_and_print(sys.argv[1])
elif len(sys.argv) >= 2:
    for passedParameter in sys.argv[1:]:
        if os.path.isfile(passedParameter):
            count_and_print(passedParameter)
        else:
            print("Passed parameter is not a file")
