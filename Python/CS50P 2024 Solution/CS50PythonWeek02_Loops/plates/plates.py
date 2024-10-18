def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length Check
    if len(s) < 2 or len(s) > 6:
        return False
    # First 2 letter check
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    # First number check
    for char in s:
        if not char.isalpha():
            if char == "0":
                return False
            else:
                break
    # Other checks
    for char in s:
        if char in ['.', ' ', '!', '?']:  #
            return False

    return True

main()
