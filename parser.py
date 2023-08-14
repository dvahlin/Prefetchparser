import pyscca
import argparse

def parse_prefetch(file_path):
    with open(file_path, 'rb') as file_object:
        scca_file = pyscca.file()
        scca_file.open_file_object(file_object)

        name = scca_file.get_executable_filename()
        lastrun = scca_file.get_last_run_time(0)
        history = scca_file.get_run_count()

        # Print static output
        print("EXECUTABLE NAME: \t{} \nRUN COUNT: \t{} \nLAST EXECUTED: \t{}".format(name, history, lastrun))
        print("\n")

        print("HISTORY:")
        history = scca_file.get_run_count()
        for run_count in range(history):
            print("Run {}: \t{}".format(run_count + 1, scca_file.get_last_run_time(run_count)))

        print("\n")

        print("RESOURCES LOADED:")
        for file_count in range(scca_file.get_number_of_filenames()):
            print(scca_file.get_filename(file_count))

def main():
    parser = argparse.ArgumentParser(description='Prefetch parser for Windows 10/11')
    parser.add_argument("-i", required=True, help="Prefetch file to parse")

    args = parser.parse_args()

    try:
        parse_prefetch(args.i)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
