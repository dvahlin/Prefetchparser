import pyscca
import os
import sys
import getopt
import argparse

def main():
    parser = argparse.ArgumentParser(description='Prefetch parser for Windows 10')
    parser.add_argument("-i", required=True, help="Prefetchfile to parse")

    args = parser.parse_args()
    i = args.i

    file_object = open(i, 'rb')
    scca_file = pyscca.file()
    scca_file.open_file_object(file_object)

    name = scca_file.get_executable_filename()
    lastrun = scca_file.get_last_run_time(0)
    history = scca_file.get_run_count()
    resources = scca_file.get_filename(0)
    totalfilenames = scca_file.get_number_of_filenames()

    # Print static output
    print("EXECUTABLE NAME: \t{} \nRUN COUNT: \t{} \nLAST EXECUTED: \t{}".format(name,history,lastrun))

    print("\n")

    print("HISTORY:")
    for run_count in range(scca_file.get_run_count()):
        print(scca_file.get_last_run_time(run_count))

    print("\n")

    print("RESOURCES LOADED:")
    for file_count in range(scca_file.get_number_of_filenames()):
        print(scca_file.get_filename(file_count))

if __name__ == '__main__':
    main()
