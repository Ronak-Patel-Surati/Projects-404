# An empty list for names
names = []

while True:
    try:
        name = input(" ")
        if name:
            names.append(name)
        else:
            break
    except EOFError:
        break

# Print the Adieu message
print("Adieu, adieu, to", end=" ")

if len(names) > 2:
    for n in names[:-1]:
        print(n, end=", ")
    print("and", names[-1])
elif len(names) == 2:
    print(f"{names[0]} and {names[1]}")
elif len(names) == 1:
    print(names[0])
else:
    pass
