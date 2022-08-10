import random

def main():

    counter = 0
    score = 0

    level = get_level()

    while counter < 10:
        result = generate_integer(level)

        if result:
            score += 1
            counter += 1
        else:
            counter += 1

    print(int(score))

def get_level():
    while True:
        try:
            n = int(input('Level: '))
        except:
            pass

        try:
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    tries = 0

    if level == 1:
        x = random.choice(range(0, 10))
        y = random.choice(range(0, 10))

    elif level == 2:
        x = random.choice(range(10, 99))
        y = random.choice(range(10, 99))

    elif level == 3:
        x = random.choice(range(100, 999))
        y = random.choice(range(100, 999))

    while True:

        try:
            z = (input(f'{x} + {y} = '))

        except:
            pass

        try:
            if x + y == int(z):
                return True
        except:
            pass

        try:
            if x + y != z:
                tries += 1
                print('EEE')
        except:
            pass

        try:
            if tries == 3:
                print(f'{x} + {y} = {x + y}')
                return False
        except:
            pass


# Create a while loop outside of generate_integer()
# Use generate_integer() to generate the equation/value only
# Use counters and markers outside of the function to retain purity


if __name__ == "__main__":
    main()