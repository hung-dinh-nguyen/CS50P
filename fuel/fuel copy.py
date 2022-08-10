def main():
    '''
1. split('/') the string and put into an array/list
2. convert str elements in the list to int()
    a) If error, pass the input again
3. IF statement to check if X (numerator) is greater than Y (denominator)
    a) if Yes, pass the input again
    b) if NO, look at 4
4. IF statement to check if Y == 0
    a) if Yes, pass the input again
    b) if NO, look at 5
5. variable = X/Y * 100
6. print(f'{variable}%')
'''
    def compare(value):
        while True:
            fraction = input(value)
            fraction_list = fraction.split('/')

            try:
                return round((int(fraction_list[0]) / int(fraction_list[1]) * 100))
            except (ZeroDivisionError, ValueError):
                pass

    def level(gauge):
        if 99 <= gauge <= 100:
            return print('F')
        elif 1 < gauge < 99:
            return print(f'{gauge}%')
        elif 0 <= gauge <= 1:
            return print('E')

    percent = compare('Fraction: ')

    while percent < 0 or percent > 100:
        percent = compare('Fraction: ')

    level(percent)

main()


----------