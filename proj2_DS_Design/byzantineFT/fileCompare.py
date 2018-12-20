import filecmp
import sys
import argparse


def compare_file(file1, file2):
    if file1 == "" or file2 == "":
        print('File path empty!')
        sys.exit()
    else:
        print("Comparing {0} and {1}".format(file1, file2))
    
      
    result = filecmp.cmp(file1,file2)
    return result



if __name__ == "__main__":
    # To define two arguments should be passed in, and usage: -f1 fname1 -f2 fname2
    my_parser = argparse.ArgumentParser(description="Two arguments should be passed in")
    my_parser.add_argument('-f1', action='store', dest='fname1', required=True)
    my_parser.add_argument('-f2', action='store', dest='fname2', required=True)
    # retrieve all input arguments
    given_args = my_parser.parse_args()
    file1 = given_args.fname1
    file2 = given_args.fname2
    result = compare_file(file1, file2)
    print("Compare result:",result)
