#!/usr/bin/env python
import sys
import os

fileName = os.path.basename(sys.argv[1])
file = open(sys.argv[1], 'r')
lineCount = 0
wordCount = 0
charCount = 0

for line in file.readlines():
    lineCount += 1
    print(len(line))
    charCount += len(line)
    for word in line.split():
        wordCount += 1
file.close()
print(lineCount, wordCount, charCount, fileName)
