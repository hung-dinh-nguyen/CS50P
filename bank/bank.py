def main():
    greeting = input('What is the greeting? ')
    print(greeting)
    print(value(greeting))


def value(greeting):

    format_greeting = greeting.lower().strip()

    if format_greeting.find('hello') == 0:
        return '$0'
    elif format_greeting.find('h') == 0:
        return '$20'
    else:
        return '$100'

if __name__ == '__main__':
    main()




