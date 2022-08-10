def main():

    print(lines_counter())

def lines_counter():
    import sys

    if len(sys.argv) != 2:
        sys.exit('Not 2 command-line arguments')

    elif sys.argv[1].find('.py') == -1:
        sys.exit('Not a Python file')

    try:
        with open(sys.argv[1]) as file:
            reader = file.readlines()
            counter = 0

            for i in range(len(reader)):
                reader[i] = reader[i].strip()

            for row in reader:
                if row.startswith('#'):
                    counter += 0
                elif row == '':
                    counter += 0
                else:
                    counter += 1

            return counter

    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == "__main__":
    main()


"""

1. Check if argv[1] contains .py and len(argv) == 2
    a) else sys.exit('')
2. Check if argv[1] is an existing file in directory
    a) Make a try/except statement
        i) Create a with/as function
    b) if it goes to except, sys.exit('')
3. Create a FOR row IN file loop
    a) If row.startswith('#')
        i) counter += 0
    b) If re.search('^\s+\s$', row):
        i) counter += 0
    c) Else
        i) counter += 1

"""