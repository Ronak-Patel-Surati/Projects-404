#input le
# camle somehwo
#coco?
#take input
camelCase = input("What's your name Beauty? ")
print("Your CamelCase: " + camelCase)

#try 4
for _ in camelCase:
    if _.isupper():
        print("_" + _.lower(), end='')
    else:
        print(_, end='')
print()

