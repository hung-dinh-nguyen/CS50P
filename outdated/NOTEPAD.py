
    '''
    1. Create a function that takes an input
    2. return split('/') that input
        a. If error, pass
    3. return split(' ') that input
        a. if error, pass
    4. Create another function of try/except
    5. return int(str)
        a. If error, pass
        b. If not, print(year-month-date)
    6. return new_list = [list[0], list[1][0], list[2]]

    7. Create a dictionary with list of month names & number values
    8. Use the dict to place value on the Month Names in String
    9. TBD
'''

    month_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October":10,
    "November": 11,
    "December": 12,
    }


    def convert(prompt):
        while True:
            date = input(prompt)

            try:
                return date.split('/')
            except:
                pass

            try:
                return date.split(' ')
            except:
                pass

################## Converts elements in list to integers

    def checker(format):
        for i in range(len(date_list)):
            date_list[i] = int(date_list[i])

        print(f'{date_list[2]}-{date_list[0]:02d}-{date_list[1]:02d}')



    date_list = convert('What is the date? ')

########################### Converts Month Names to integers

    def check(format):
        for month in months:
            if format[0] == month:
                format[0] = months[month]
                for i in range(len(format)):
                    format[i] = int(format[i])
            else:
                format = convert('What is the date? ')
        else:
            for i in range(len(format)):
                format[i] = int(format[i])

#################### make sure values are not over reasonable numbers for months and dates and years
    final_date
    if final_date[0] < 1 or final_date[1] < 1 or 12 < final_date[1] or final_date[2] < 1 or 31 < final_date[2]:
        restart the input





            if final_date[2] < 1 or final_date[0] < 1 or 12 < final_date[0] or final_date[1] < 1 or 31 < final_date[1]:
        return main()

    print(f'{final_date[2]}-{final_date[0]:02d}-{final_date[1]:02d}')


    ####### 111111111
def main():
    '''
    1. Create a function that takes an input
    2. return split('/') that input
        a. If error, pass
    3. return split(' ') that input
        a. if error, pass
    4. Create another function of try/except
    5. return int(str)
        a. If error, pass
        b. If not, print(year-month-date)
    6. return new_list = [list[0], list[1][0], list[2]]

    7. Create a dictionary with list of month names & number values
    8. Use the dict to place value on the Month Names in String
    9. TBD
'''

    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October":10,
    "November": 11,
    "December": 12,
    }


    def convert(prompt):
        while True:
            date = input(prompt)

            try:
                if len(date.split('/')) > 1:
                    return date.split('/')
            except:
                pass

            try:
                return date.split(' ')
            except:
                pass

    def checker(format):
        try:
            for i in range(len(format)):
                format[i] = int(format[i])
            return format
        except:
            pass
        try:
            for month in months:
                if format[0] == month:
                    format[0] = months[month]
                    format[1] = format[1][:-1]
                    for i in range(len(format)):
                        format[i] = int(format[i])
                    return format
        except:
            return main()

    date_list = convert('What is the date? ')
    final_date = checker(date_list)

    if final_date[2] < 1 or final_date[0] < 1 or 12 < final_date[0] or final_date[1] < 1 or 31 < final_date[1]:
        return main()

    print(f'{final_date[2]}-{final_date[0]:02d}-{final_date[1]:02d}')


main()







###### 2 222222222222222222222

    def main():
    '''
    1. Create a function that takes an input
    2. return split('/') that input
        a. If error, pass
    3. return split(' ') that input
        a. if error, pass
    4. Create another function of try/except
    5. return int(str)
        a. If error, pass
        b. If not, print(year-month-date)
    6. return new_list = [list[0], list[1][0], list[2]]

    7. Create a dictionary with list of month names & number values
    8. Use the dict to place value on the Month Names in String
    9. TBD
'''

    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October":10,
    "November": 11,
    "December": 12,
    }


    def convert(prompt):
        while True:
            date = input(prompt)

            try:
                if len(date.split('/')) > 1:
                    return date.split('/')
            except:
                pass

            try:
                return date.split(' ')
            except:
                pass

    def checker(format):
        try:
            for i in range(len(format)):
                format[i] = int(format[i])
            return format
        except:
            pass
        try:
            for month in months:
                if format[0] == month:
                    format[0] = months[month]
                    format[1] = format[1][:-1]
                    for i in range(len(format)):
                        format[i] = int(format[i])
                    return format
        except:
            return main()

    def final_checker(final_date):
        try:
            if final_date[2] < 1 or final_date[0] < 1 or 12 < final_date[0] or final_date[1] < 1 or 31 < final_date[1]:
                return main()
        except:
                return main()

    date_list = convert('What is the date? ')
    checked_list = checker(date_list)
    final_date = final_checker(checked_list)


    print(f'{final_date[2]}-{final_date[0]:02d}-{final_date[1]:02d}')

main()