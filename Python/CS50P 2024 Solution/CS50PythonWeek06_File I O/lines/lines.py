from sys import exit, argv

if len(argv) != 2:
    if len(argv) < 2:
        exit("Too few command-line arguments")
    else:
        exit("Too many command-line arguments")

FileName = argv[1] #CamelCase


Extension = FileName.find(".")
if FileName[Extension:] != '.py':
    exit('Not a Python file')

LineCount = 0

try:
    with open(FileName) as File:
        for line in File:
            if line.isspace():
                continue
            if line.strip().startswith('#'):
                continue
            LineCount += 1

except FileNotFoundError:
    exit("File does not exist")

print("Line count:", LineCount)
