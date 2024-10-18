#To Do


def main():
    while True:
        user_input = input("Date: ").strip()
        try:
            if '/' in user_input:
                month, day, year = map(int, user_input.split('/'))
            else:
                parts = user_input.split()
                if len(parts) == 2:
                    raise ValueError
                month, day, year = parts[0], int(parts[1].strip(',')), int(parts[2])
                month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"].index(month) + 1
            if 1 <= month <= 12 and 1 <= day <= 31 and year > 1500: #wanted to do so
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
            else:
                raise ValueError
        except (ValueError, IndexError):
            print("Invalid date format. Please try again.")


main()
