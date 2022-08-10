import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_list = re.findall(r'\bum\b', s, re.IGNORECASE)
    um_counter = len(um_list)

    return um_counter

if __name__ == "__main__":
    main()