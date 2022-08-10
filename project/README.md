# Roman Numeral Converter
## Video Demo:  https://youtu.be/zo9VL08gXGs

## Description:

This project is a Roman Numeral Converter. It takes a number and displays its equivalent Roman Numeral.
The Program is separated into 4 parts. 1st is main(), 2nd is input_check(), 3rd is roman_convert(), and 4th is combine().

The main() function asks for an input and calls the remaining functions to perform the conversion. In this function, the input can be a string of anything. Then, this value is inputted into input_check() to see if it can be parsed into an integer. Afterward, the integer is inputted into roman_convert() to create a list of Roman Numerals. Next, that list is inputted into combine() to create the final Roman Numeral string. Finally, that string is printed.

The input_check() function is used to determine whether the input from main() can be converted to an integer. If it can, the function will return the input as an integer. If not, the program will stop and raise a ValueError.

The roman_convert() produces a list of Roman Numeral symbols. First, a Dictionary of Roman Numerals and its equivalent values are created. Then, an empty list and a copy of the input. A local function called push_numerals() is created within the roman_convert() function. The push_nuemrals() function is a recursion function. The function is a series of if/elif statements performing subtraction on a copy of the input, appending a Roman Numeral to the list, and returning the push_numerals() function. The copy is subtracted by the greatest value in Roman Numerals Dictionary. And if the result is a positive number or 0, that Roman Numeral is append() to a list. If the subtraction were to result in a negative number, the next greatest value in the Roman Numeral Dictionary will be utilized. This will continue until the input copy is equal to zero. Once the recursion function is complete, the roman_convert() function will return the list of Roman Numerals.

The combine() function "".join() the Roman Numeral lists. So, a single Roman Numeral String is produced. This string is returned.

There is also an if __name__ == '__main__' statement, so each function can be properly unit tested and be utilized in other programs if needed.
