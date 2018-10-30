import sys
import re


def remove_line_endings(array):
    temp_array=[]
    for string in array:
        temp_array.append(re.sub("\n", "", string))
    return temp_array


def main():
    og_file = open(sys.argv[1], 'r')
    rm_file = open(sys.argv[2], 'r')

    original_file1 = list(og_file)
    modified_file1 = list(rm_file)

    original_file = remove_line_endings(original_file1)
    modified_file = remove_line_endings(modified_file1)

    for i, original_line in enumerate(original_file):
        temp_array = []
        for j in range(i, len(modified_file)):
            if original_line == modified_file[j]:
                for t in temp_array:
                    print("+ " + t)
                print("0 " + original_line)
                break
            if j == len(modified_file)-1:
                modified_file = modified_file[:i+1] + [original_line] + modified_file[i+1:]
                print("- " + original_line)
            temp_array.append(modified_file[j])
        if i == len(original_file)-1 and i < len(modified_file)-1:
            for x in range(len(modified_file)-(len(modified_file)-len(original_file))+1, len(modified_file)):
                print("+ " + modified_file[x])
    og_file.close()
    rm_file.close()


main()