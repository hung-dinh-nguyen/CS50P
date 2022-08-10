def main():
    import pyfiglet
    import sys

    if len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            if pyfiglet.Figlet(font = sys.argv[2]) != None:
                text = input('Input: ')
                font = pyfiglet.Figlet(font = sys.argv[2])
                print(font.renderText(text))
        else:
            sys.exit('Invalid Usage')
    elif len(sys.argv) == 1:
        text = input('Input: ')
        font = pyfiglet.Figlet(font = 'standard')
        print(font.renderText(text))
    else:
        sys.exit('Invalid Usage')


main()