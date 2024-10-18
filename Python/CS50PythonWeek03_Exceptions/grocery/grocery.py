# create a unintialized dic
#take inputs in dict #while loop
#sorted it
#uppercase
#output shoulde have been index
def main():
    grocery_list = {}
    try:
        while True:
            item = input().strip().lower()
            if item:
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1
    except EOFError:
        pass

    # Converting items to uppercase and outputting with count
    for item, count in sorted(grocery_list.items()):
        print(f"{count} {item.upper()}")

main()


