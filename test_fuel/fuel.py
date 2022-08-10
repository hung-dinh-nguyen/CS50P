def main():

    fraction = input('Fraction: ')
    percentage = convert(fraction)
    fuel_gauge = gauge(percentage)

    print(fuel_gauge)

def convert(fraction):
        while True:
            fraction_list = fraction.split('/')

            if round((int(fraction_list[0]) / int(fraction_list[1]) * 100)) > 100:
                fraction = input('Fraction: ')
                return convert(fraction)
            else:
                return round((int(fraction_list[0]) / int(fraction_list[1]) * 100))


def gauge(percentage):

    try:
        if 99 <= percentage <= 100:
            return 'F'
        elif 1 < percentage < 99:
            return f'{percentage}%'
        elif 0 <= percentage <= 1:
            return 'E'
    except:
        return ''

if __name__ == "__main__":
    main()