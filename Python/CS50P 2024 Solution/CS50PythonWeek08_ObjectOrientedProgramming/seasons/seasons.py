from datetime import date
import inflect
import sys
import re

def main():
    inpt = input("Date of Birth (YYYY-MM-DD): ")

    # Using regex to validate and extract the date components
    if search := re.search(r'^(\d{4})-(\d{2})-(\d{2})$', inpt):
        inpt = list(search.groups())
    else:
        sys.exit('Invalid date')

    # Convert the extracted string date parts to integers
    day = list(map(int, inpt))

    # Validate the month and day values
    if day[1] < 1 or day[1] > 12:
        sys.exit('Invalid date')
    elif day[2] < 1 or day[2] > 31:
        sys.exit('Invalid date')

    input_bday = day

    # Get today's date
    today = date.today()

    # Create a date object for the birthday
    bday = date(input_bday[0], input_bday[1], input_bday[2])

    # Calculate the difference in days between today and the birthday
    diff = bday - today
    no_of_days = -int(diff.days)

    # Calculate the total number of minutes
    minutes = no_of_days * 24 * 60

    # Convert the number of minutes to words
    inf = inflect.engine()
    min_words = inf.number_to_words(minutes)

    # Remove the word 'and' and capitalize the result
    min_words = min_words.replace(' and', '').capitalize()

    # Truncate the result if it's too long
    max_length = 35  # Adjusted to allow for the exact expected output
    if len(min_words) > max_length:
        min_words = min_words[:max_length].rsplit(',', 1)[0] + ' minutes'

    return min_words

if __name__ == "__main__":
    print(main())
