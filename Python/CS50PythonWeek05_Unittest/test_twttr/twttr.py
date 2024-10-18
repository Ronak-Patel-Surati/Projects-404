# code i used in pset2
# line = input("Input: ")
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# for letter in vowels:
#    line = line.replace(letter, "")
#
# print("Output:", line)


def main():
    line = input("Input: ")
    line = shorten(line)
    print("Output:", line)


def shorten(line):
    # restructuring  my own code
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in vowels:
        line = line.replace(letter, "")
    return line


if __name__ == "__main__":
    main()
