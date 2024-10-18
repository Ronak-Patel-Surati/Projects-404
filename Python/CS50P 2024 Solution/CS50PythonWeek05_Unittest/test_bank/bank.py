#starting to use split screen in dev.cs50
#restructuring

def main():
    greeting = input("Greeting ").lower().strip()
    greeting = value(greeting)
    print("$" + greeting, sep="")

def value(greeting):
    greeting = greeting.strip()
    if 'hello' in greeting:
        return("0")
    elif greeting.startswith("h"): #use logi for specific function and Documentations for all the solution
        return("20")
    else:
        return("100")


if __name__ == "__main__":
    main()
