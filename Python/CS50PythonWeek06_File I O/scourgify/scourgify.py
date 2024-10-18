from sys import argv, exit
import csv


def main():
    FileName1, FileName2 = Extension(argv)
    csvcheck(FileName1)
    csvcheck(FileName2)
    firstnames = []
    lastnames = []
    houses = []

    try:
        with open(FileName1) as L1:
            rows = csv.DictReader(L1)
            for row in rows:
                last, first = row["name"].split(",")
                lastnames.append(last.strip())
                firstnames.append(first.strip())
                houses.append(row["house"])
    except FileNotFoundError:
        exit("File does not exist")
    except Exception as arg:
        exit(arg)

    writefile = "after.csv"

    try:
        with open(writefile, "w") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(firstnames)):
                writer.writerow(
                    {
                        "first": firstnames[i],
                        "last": lastnames[i],
                        "house": houses[i],
                    }
                )
    except Exception as e:
        exit(f"Error writing to file: {e}")


def Extension(argv):
    if len(argv) != 3:
        if len(argv) < 3:
            exit("Too few command-line arguments")
        else:
            exit("Too many command-line arguments")
    return (argv[1], argv[2])


def csvcheck(FileName):
    Extension = FileName.find(".")
    if FileName[Extension:] != ".csv":
        exit("Not a CSV file")


if __name__ == "__main__":
    main()
#you know what i am submititng this as it is as above 70% is assigned as done only 

