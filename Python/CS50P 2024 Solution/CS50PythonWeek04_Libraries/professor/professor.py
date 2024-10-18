import random

# template


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        ans = str(x + y)
        res = 0

        for i in range(4):
            if i == 3:
                print(x, "+", y, "=", ans)
                break

            print(x, "+", y, "=", end=" ")
            userinput = input()
            if userinput != ans:
                print("EEE")
            else:
                score += 1
                break

    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            return level if level in range(1, 4) else raise_exception()  #fixed the first test issue by replacing 0 with 1
        except Exception:
            pass  # Catching all exceptions for simplicity


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


def raise_exception():
    raise Exception


if __name__ == "__main__":
    main()
