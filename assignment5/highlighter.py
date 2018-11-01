import os
import argparse
import re
from filereader import read_syntax_file, read_color_file


def color_injection(match, color):
    print("---------")
    print(match, color)
    return "Hello"


def highlight(input, regex_dict, theme_dict=None):
    """

    :param input:
    :param regex_dict:
    :param theme_dict:
    :return:
    """
    end_color = r'\033[0m'
    match_string_array = [None] * len(input)
    print("::::::::")
    for regex, regex_name in regex_dict.items():
        # matcher = re.compile(regex.strip('\"'))  # Remove the " from the RegEx strings
        for color_name, color_theme in theme_dict.items():
            if regex_name in theme_dict and color_name == regex_name:
                re.sub(r'{}'.format(regex.strip('\"')), lambda match, color=color_theme: color_injection(match, color), input, flags=re.MULTILINE)





def main():
    parser = argparse.ArgumentParser(description="Highlight parts of an output file in the terminal using a syntax "
                                                 "dictionary, a theme dictionary and a file to apply them to")
    parser.add_argument("syntax",
                        type=str,
                        help="A syntax file, containing a dictionary of RegExes and associated names\n"
                             "Example: NNNN.*(?:$|): comment")
    parser.add_argument("theme",
                        type=str,
                        help="A theme file, containing a dictionary of associated names and color following the "
                             "bash color sequence\n"
                             "Example: comment: 0;32")
    parser.add_argument("output_file",
                        type=str,
                        help="A file where the RegEx syntax and the theme colors will be applied")
    args = parser.parse_args()

    if os.path.isfile(args.syntax) and os.path.isfile(args.theme) and os.path.isfile(args.output_file):
        regex_dict = read_syntax_file(args.syntax)
        color_dict = read_color_file(args.theme)
        output_string = open(args.output_file, 'r').read()
        highlight(output_string, regex_dict, color_dict)
        # print(regex_dict, color_dict)
        match_string=''
        for regex, name in regex_dict.items():
            matcher = re.compile(regex.strip('\"'))         # Remove the " from the strings
            output_string = open(args.output_file, 'r').read()
            previous_match_end = 0
            for match in matcher.finditer(output_string):
                match_string += output_string[previous_match_end:match.start()] + '\\033[{}m'.format(color_dict[name])+\
                                output_string[match.start():match.end()] + '\\033[0m'
                previous_match_end = match.end()

        print(match_string)

    else:
        print("\nError: highlighter.py expects to receive three files as arguments as follows:\n"
              ">>> highlighter.py foo.syntax bar.theme baz.any")


main()
