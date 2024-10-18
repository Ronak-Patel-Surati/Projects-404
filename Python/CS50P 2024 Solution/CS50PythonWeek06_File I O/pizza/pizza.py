from sys import exit, argv
import csv
from tabulate import tabulate  # type: ignore

# main
def main():
    FileName = Extension(argv)
    csvcheck(FileName)
    try:
        with open(FileName) as File:
            red = csv.reader(File)
            table = []
            headers = list(next(red))
            for row in red:
                table.append([row[0], row[1], row[2]])
        print(tabulate(table, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        exit("File does not exist")
    except Exception as arg:
        exit(str(arg))


# extension reuse from problemset 1# arguments check
def Extension(argv):
    if len(argv) != 2:
        if len(argv) < 2:
            exit("Too few command-line arguments")
        elif len(argv) > 2:
            exit("Too many command-line arguments")
    return argv[1]


# CSV check
def csvcheck(FileName):
    Extension = FileName.find(".") 
    if FileName[Extension:] != ".csv":
        exit("Not a CSV file")


if __name__ == "__main__":
    main()

    # i should boilerplate for myself # add it to pending tasks
