from validators import email


def main():
    UserInput = input("What is your email address? ").strip()

    if email(UserInput) == True:
        print("Valid")
    else:
        print("Invalid")
if __name__ == "__main__":
    main()
