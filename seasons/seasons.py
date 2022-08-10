from datetime import date
import datetime
import re
import sys
import inflect

"""
1. Take input of birth in YYYY-MM-DD format
2. Separate into year, month, and date variable
3. Create a class date() instanace of it
4. Create an instance of today's date
5. Subtract both dates
6. Convert division to seconds
7. Input the seconds into inflect
7. Inflect will convert numbers to words
"""

def main():

    b_day = birthday(input('When is your birthday? '))
    delta = difference(b_day)
    seconds = convert(delta)

    print(seconds)

def birthday(dob):

    if re.search(r'\d\d\d\d-\d\d-\d\d', dob):
        dob_list = dob.split('-')

        year = int(dob_list[0])
        month = int(dob_list[1])
        day = int(dob_list[2])

        return date(year, month, day)

    else:
        sys.exit('Incorrect Format - Example: YYYY-MM-DD')

def difference(birthday):
    t_day = datetime.date.today()

    return t_day - birthday

def convert(delta):
    p = inflect.engine()

    seconds = int(delta.total_seconds())
    minutes = int(seconds / 60)

    return f"{p.number_to_words(minutes, andword='')} minutes".capitalize()

if __name__ == "__main__":
    main()