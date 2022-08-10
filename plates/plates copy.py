import re

def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or 6 < len(s):
        return False
    elif re.search('[A-Z]+\d+[A-Z]+', s):
        return False
    elif re.search('^[A-Z]+0', s):
        return False
    elif re.search('\s', s):
        return False
    elif re.search('\W', s):
        return False
    elif re.search('[A-Z][A-Z].*', s):
        return True

main()