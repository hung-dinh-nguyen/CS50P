def main():

    """
    1. Create an empty list
    2. Create a function
    3. Add a While True Loop
    4. Ask for an input
    5. .push(input) to the empty list
    6. end when ctrl+D is hit
    7. Create Series of If Statements
        a) 1st will ask if len(list) == 1
            i) If so, print(Adieu, adieu, to + list[0])
        b) 2nd will ask if len(list) == 2
            i) If so, print(Adieu, adieu, to + list[0] + ', and' + list[1])
        c) 3rd will ask if len(list) >= 3
            i) create a new list with the first element 'Adieu, adieu, to '
            ii) Create for loop that new_list.push(i), but ends exclusively 2 indexes from the last
            iii) Join new_list
            iv) Print new_list
    """

    def add_name():
        while True:
            try:
                name = input()
                name_list.append(name)
            except EOFError:
                break

    def farewell(names):
        if len(names) == 1:
            print(f'Adieu, adieu, to {names[0]}')
        elif len(names) == 2:
            print(f'Adieu, adieu, to {names[0]} and {names[1]}')
        else:
            new_list = ['Adieu, adieu, to']
            for i in range(len(names) - 2):
                new_list.append(f'{names[i]},')
            new_list.append(f'{names[-2]}, and {names[-1]}')
            return print(' '.join(new_list))

    name_list = []
    add_name()
    farewell(name_list)


main()