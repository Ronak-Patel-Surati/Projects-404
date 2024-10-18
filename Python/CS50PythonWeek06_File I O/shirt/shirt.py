from sys import argv, exit
import os
from PIL import ImageOps as iops, Image as picture


def main():
    a, b = get_name(argv)
    check(a, b)

    # images part
    try:
        shirt = picture.open("shirt.png")
        muppet = picture.open(a)

    except FileNotFoundError:
        exit("Input does not exist")

    except Exception as exp:
        exit(str(exp))

    size = shirt.size
    muppet = iops.fit(muppet, size)
    muppet.paste(shirt, (0, 0), shirt)
    muppet.save(b)


def get_name(argv):
    if len(argv) != 3:
        if len(argv) < 3:
            exit("Too few command-line arguments")
        else:
            exit("Too many command-line arguments")
    return argv[1], argv[2]


def check(inpt, outpt):
    in_root, in_ext = os.path.splitext(inpt)
    out_root, out_ext = os.path.splitext(outpt)
    if in_ext.lower() != out_ext.lower():
        exit("Input and output have different extensions")
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if in_ext.lower() not in valid_extensions:
        exit("Invalid input")
    if out_ext.lower() not in valid_extensions:
        exit("Invalid output")


if __name__ == "__main__":
    main()
