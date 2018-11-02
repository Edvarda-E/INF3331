import os
import argparse
import re
from filereader import read_syntax_file


def main():
    """
    Parses positional arguments and highlights an input file based on the given RegEx and theme colors given
    from the terminal

    Arguments:
        input file (file):  An arbitrary file with contents to be outputted to the terminal
        syntax file (file): A .syntax file as a RegEx dictionary

    Returns:
        Calls the highlight function that prints the matched output to the terminal
    """
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
        for line in output_string:
            processed_line = re.sub("\n", "", line)
            for regex, name in regex_dict.items():
                processed_regex = regex.strip('\"')                 # Remove the " from the strings
                matcher = re.compile(processed_regex)
                if matcher.search(processed_line):
                    if args.highlighter:
                        previous_match_end = 0
                        match_string = ""
                        # Color array to cycle of infinitely
                        colours = [
                            31,  # red
                            32,  # green
                            33,  # yellow
                            34,  # blue
                            35   # magneta
                        ]
                        for match in matcher.finditer(line):
                            match_string += line[previous_match_end:match.start()] +  \
                                            f'\033[{colours[infinite_iterator]}m' + \
                                            line[match.start():match.end()] + f'\033[0m'
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
