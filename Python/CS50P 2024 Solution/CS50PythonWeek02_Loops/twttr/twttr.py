line = input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for letter in vowels:
    line = line.replace(letter, "")

print("Output:", line)
