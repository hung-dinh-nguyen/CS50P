import validators

def main():
    print(checker(input('Email: ')))

def checker(s):
    if validators.email(s):
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == '__main__':
    main()