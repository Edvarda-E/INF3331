import os
import sys
from filereader import read_syntax_file


def main():
    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        dict = read_syntax_file(sys.argv[1])
        print(dict)

main()