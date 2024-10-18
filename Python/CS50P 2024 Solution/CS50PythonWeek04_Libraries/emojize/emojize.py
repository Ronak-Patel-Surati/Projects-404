def main():
    user = input("Input: ").strip()
    words = user.split(" ")
    result = []
    for word in words:
        result.append(runmatch(word.lower()))
    print(" ".join(result))


def runmatch(word):
    match word:
        case ":1st_place_medal:":
            return "🥇"
        case ":thumbsup:":
            return "👍"
        case ":earth_asia:":
            return "🌏"
        case ":candy:":
            return "🍬"
        case ":ice_cream:":
            return "🍨"
        case _:
            return word


if __name__ == "__main__":
    main()
