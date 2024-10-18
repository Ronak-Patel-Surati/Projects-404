#take input
num = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
num = num.strip().lower()
#use match
if num == "forty-two"  or num == "forty two" or num == "42":
    print("Yes")
else:
    print("No")

