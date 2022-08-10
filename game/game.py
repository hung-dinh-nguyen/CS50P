def main():
    '''
    1. Create a RandNum Function
        note: while True loop
        a) Ask for an input and make it equal n
            i) input cannot be n < 1
            ii) If so, ask again
        b) Create a list with range(1, n+1)
        c) return randon.choice(list)
    2. Create Guess Function
        note: while True Loop
        a) Paramter will be return value from Range List Function
        b) Ask for input to try to guess Parameter
        c) If less than, print(too small)
        d) If greater than, print(too large)
        e) If equal too, print(just right) & break loop

    '''

    import random
    import sys

    def rand_num(prompt):
        while True:
            try:
                n = int(input(prompt))
                break
            except:
                pass

        if n < 1:
            return rand_num(prompt)
        else:
            rand_list = list(range(1, n + 1))
            return random.choice(rand_list)

    def guesser(answer):
        while True:
            try:
                guess = int(input('Guess: '))

                if guess > answer:
                    print('Too large!')
                elif guess < answer:
                    print('Too small!')
                elif guess == answer:
                    return print('Just right!')
            except:
                pass


    answer = rand_num('Level: ')
    guesser(answer)


main()