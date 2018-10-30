import os
import argparse
import re
from filereader import read_syntax_file, read_color_file


def main():
    parser = argparse.ArgumentParser(description="Diff colorization")
    parser.add_argument("input",
                        type=str,
                        help="Input file with content to be matched")
    parser.add_argument("syntax",
                        type=str,
                        help="A syntax file, containing a dictionary of RegExes and associated names\n")
    parser.add_argument("theme",
                        type=str,
                        help="A theme file, containing a dictionary of associated names and color following the ")
    args = parser.parse_args()

    if os.path.isfile(args.input) and os.path.isfile(args.syntax) and os.path.isfile(args.theme):
        regex_dict = read_syntax_file(args.syntax)
        color_dict = read_color_file(args.theme)
        output_string = list(open(args.input, 'r').readlines())
        for regex, name in regex_dict.items():
            processed_regex = regex.strip('\"')                 # Remove the " from the strings
            matcher = re.compile(processed_regex)
            for line in output_string:
                if matcher.search(line) and name == "unchanged":
                    print(line)
                elif matcher.search(line) and color_dict[name] and name != "unchanged":
                    print(r'\033[{}m'.format(color_dict[name]) + line + r'\033[0m')
    else:
        print("\nError: diff_demo.py expects to receive two files as arguments as follows:\n"
              ">>> grep.py foo.syntax")


if __name__ == '__main__':
    main()
