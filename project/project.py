# Roman Numeral Converter

"""
note: Create a Roman Numeral Dict from I to M

1. 1st Function validates that the input can become an int()
2. 2nd Function applies the Roman Numeral Dict on the input
    a) Reduce the value of the input by the largest Dict key
        i) If subtraction will result in negative value, use the next key/value
    b) Repeat until value == 0
3. 3rd Function will combine the list of Roman Numerals

"""

def main():

    string = input('Number: ')
    number = input_check(string)
    list = roman_convert(number)
    roman_numeral = combine(list)

    print(roman_numeral)

def input_check(string):

    try:
        number = int(string)
    except:
        raise ValueError

    return number

def roman_convert(number):
    roman_dict = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C':100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
  }

    copy = number
    list = []

    def push_numerals(number_copy, roman_list):
        while number_copy > 0:
            if number_copy - roman_dict['M'] >= 0:
                number_copy -= roman_dict['M']
                roman_list.append('M')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['CM'] >= 0:
                number_copy -= roman_dict['CM']
                roman_list.append('CM')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['D'] >= 0:
                number_copy -= roman_dict['D']
                roman_list.append('D')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['CD'] >= 0:
                number_copy -= roman_dict['CD']
                roman_list.append('CD')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['C'] >= 0:
                number_copy -= roman_dict['C']
                roman_list.append('C')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['XC'] >= 0:
                number_copy -= roman_dict['XC']
                roman_list.append('XC')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['L'] >= 0:
                number_copy -= roman_dict['L']
                roman_list.append('L')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['XL'] >= 0:
                number_copy -= roman_dict['XL']
                roman_list.append('XL')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['X'] >= 0:
                number_copy -= roman_dict['X']
                roman_list.append('X')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['IX'] >= 0:
                number_copy -= roman_dict['IX']
                roman_list.append('IX')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['V'] >= 0:
                number_copy -= roman_dict['V']
                roman_list.append('V')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['IV'] >= 0:
                number_copy -= roman_dict['IV']
                roman_list.append('IV')
                return push_numerals(number_copy, roman_list)

            elif number_copy - roman_dict['I'] >= 0:
                number_copy -= roman_dict['I']
                roman_list.append('I')
                return push_numerals(number_copy, roman_list)

    push_numerals(copy, list)

    return list

def combine(list):
    return "".join(list)

if __name__ == '__main__':
    main()