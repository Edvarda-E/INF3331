import sys


def main():
    og_file = open(sys.argv[1], 'r')
    rm_file = open(sys.argv[2], 'r')

    original_file = list(og_file)
    modified_file = list(rm_file)\

    counter = 0
    # print(modified_file.readlines())
    #print(modified_line)
    for i, original_line in enumerate(original_file):
        for j, modified_line in enumerate(modified_file):
            if original_line == modified_line:
                if i == 0 and j > 0:
                    for value in modified_file[0:j]:
                        print("+ " + value)
                print("0 " + modified_line)
            elif i != 0 and j != 0 and i != len(original_file)-1 and j!= len(modified_file)-1 and \
                    original_file[i-1] == modified_file[j-1] and original_file[i+1] == modified_file[j+1]:
                print("- " + original_line)
                print("+  " + modified_line)
                # print(j)
                counter = j
        j = counter

    og_file.close()
    rm_file.close()
main()