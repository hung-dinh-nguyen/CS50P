def main():

    reader = menu()
    print(reader)

def menu():
    import csv
    import sys
    from tabulate import tabulate


    if len(sys.argv) != 2:
        sys.exit('Not 2 command-line arguments')

    elif sys.argv[1].find('.csv') == -1:
        sys.exit('Not a CSV file')

    menu_list = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu_list.append([row[0], row[1], row[2]])
            return tabulate(menu_list, headers="firstrow", tablefmt = 'grid')

    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == '__main__':
    main()