def main():

    info = find()
    list = convert(info)
    new_list = separate(list)
    write_list = write(new_list)

"""
1. Import the necessary modules
    a) csv, sys
2. Create If Statments to sys.exit
    a) Exit if sys.argv != 3
    b) Exit if find('.csv') == -1
3.  Create a variable = csv.reader
4. Append to empty list
5. ','.Split.list[0] to separate the first and last names
6. Append to a new separate list
7. Write that to a new csv file

"""

def find():
    import sys

    if len(sys.argv) != 3:
        sys.exit('Not 3 command-line arguments')

    elif sys.argv[1].find('.csv') == -1:
        sys.exit('Not a CSV file')

    else:
        try:
            return open(sys.argv[1])

        except FileNotFoundError:
            sys.exit('File does not exist')

def convert(info):
    import csv

    info_list = []

    with info as file:
        reader = csv.DictReader(file)
        for row in reader:
            info_list.append({'name': row['name'], 'house': row['house']})

        return info_list

def separate(list):
    students_list = []

    for row in list:

        full_name = row['name'].split(',')
        first = full_name[1].strip()
        last = full_name[0].strip()

        house = row['house']

        new_row = (first, last, house)
        students_list.append(new_row)

    return students_list

def write(new_list):
    import csv
    import sys

    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames = ['first', 'last', 'house'])
        writer.writeheader()
        for row in new_list:
            writer.writerow({'first': row[0], 'last': row[1], 'house': row[2]})

if __name__ == '__main__':
    main()