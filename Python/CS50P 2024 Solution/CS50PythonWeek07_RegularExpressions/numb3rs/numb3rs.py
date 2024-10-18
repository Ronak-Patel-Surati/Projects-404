import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    bank = ip.strip().split(".")
    for block in bank:
        if len(bank) != 4:
            return False
        for block in bank:
            if not block.isdigit():
                return False
            if not 0 <= int(block) <= 255:
                return False
    return True


if __name__ == "__main__":
    main()
