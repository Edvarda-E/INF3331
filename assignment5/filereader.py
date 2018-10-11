import sys


def read_syntax_file(file):
    """
    File that processes a syntax file, turning it into a Python dictionary. Expects each line of the
    syntax file to follow the format "RegEx": name, ex. "NNNN.*(?:$|\n)": comment

    Arguments:
        file (A .syntax file): Input file with RegEx and associated names for the RegEx

    Returns
        syntax_dictionary (dictionary): Stored values from file in dictionary as ["RegEx"] = "name"

    """
    syntax_dict = {}
    try:
        with open(file, 'r') as syntax_file:        # with open() closes file automatically
            for line in syntax_file.readlines():
                if len(line.split(':')) >= 2:       # If greater than 2 there are presumably colons in the RegEx
                    # To support colons in the RegEx, I use rsplit to achieve only one split at the rightmost colon in
                    # the line, storing everything up to the last colon as regex, and everything after as name
                    regex, name = line.rsplit(':', 1)
                    # Stripping the values, removing eventual whitespace from the beginning and end of the strings
                    syntax_dict[regex.strip()] = name.strip()

                else:
                    # line.split(':') was shorter than 2, which is unexpected behavior
                    print("Problem reading syntax from the following line:\n" + line)

    except IOError as error:
        print("Error when attempting to open file: " + file + "\nError Message:" + repr(error))

    return syntax_dict
