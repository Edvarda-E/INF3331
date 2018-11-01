import os
import argparse
import re
from filereader import read_syntax_file


def main():
    parser = argparse.ArgumentParser(description="grep-like utility")
    parser.add_argument("input",
                        type=str,
                        help="Input file with content to be matched")
    parser.add_argument("syntax",
                        type=str,
                        help="A syntax file, containing a dictionary of RegExes and associated names\n")
    parser.add_argument("--highlighter",
                        action="store_true",
                        help="Color the matches")

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
                    if args.highlighter:
                        previous_match_end = 0
                        match_string = ""
                        colours = [
                            31,  # red
                            32,  # green
                            33,  # yellow
                            34,  # blue
                            35   # magneta
                        ]
                        for match in matcher.finditer(line):
                            match_string += line[previous_match_end:match.start()] +  \
                                            r'\033[{}m'.format(colours[infinite_iterator]) + \
                                            line[match.start():match.end()] + r'\033[0m'
                            print(infinite_iterator)
                            previous_match_end = match.end()
                        infinite_iterator = infinite_iterator + 1 if infinite_iterator < len(colours)-1 else 0
                        print(match_string)
                    else:
                        print(line)
    else:
        print("\nError: grep.py expects to receive two files as arguments as follows:\n"
              ">>> grep.py foo.syntax")


if __name__ == '__main__':
    main()
