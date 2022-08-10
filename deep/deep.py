def main():
    answer = input('What is the answer to the Great Question of Life, the Universe and Everything? ').lower().strip()

    def decision(ans):
        if ans == '42' or ans == 'forty two' or ans == 'forty-two':
            return 'Yes'
        else:
            return 'No'

    print(decision(answer))

main()