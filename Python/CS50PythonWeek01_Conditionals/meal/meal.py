def main():
    time = input("ENTER THE CURRENT TIME : ").strip() #spaces is headcahe
    time = convert(time)
    #logic
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
#but why seprate function if can included it one code???????????????
def convert(time):
    hours, minutes = time.split(':')
    return float(hours) + float(minutes)/60

if __name__ == "__main__":
    main()
