import os
import argparse
import re
from filereader import read_syntax_file


def main():
    parser = argparse.ArgumentParser(description="grep-like utility")
    parser.add_argument("input",
                        type=str,
                        help="Input file with content to be matched"
                             "Example: comment: 0;32")
    parser.add_argument("syntax",
                        type=str,
                        help="A syntax file, containing a dictionary of RegExes and associated names\n"
                             "Example: NNNN.*(?:$|): comment")
    parser.add_argument("--highlighter",
                        action="store_true",
                        help="Color the matches "
                             "Example: NNNN.*(?:$|): comment")

    args = parser.parse_args()

    if os.path.isfile(args.input) and os.path.isfile(args.syntax):
        regex_dict = read_syntax_file(args.syntax)
        infinite_iterator = 0
        output_string = list(open(args.input, 'r').readlines())
        for regex, name in regex_dict.items():
            processed_regex = regex.strip('\"')                 # Remove the " from the strings
            matcher = re.compile(processed_regex)
            for line in output_string:
                processed_line = re.sub("\n", "", line)
                if matcher.search(processed_line):
                    print(matcher.search(processed_line))
                    if args.highlighter:
                        colours = [
                            31,  # red
                            32,  # green
                            33,  # yellow
                            34,  # blue
                            35   # magneta
                        ]
                        match_start, match_end = matcher.search(processed_line).span()
                        print(line[:match_start] + r'\033[{}m'.format(colours[infinite_iterator])+\
                                line[match_start:match_end] + r'\033[0m' + line[match_end:])
                        infinite_iterator = infinite_iterator + 1 if infinite_iterator < len(colours)-1 else 0
                    else:
                        print(line)
    else:
        print("\nError: grep.py expects to receive two files as arguments as follows:\n"
              ">>> grep.py foo.syntax")

main()