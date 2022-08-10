def main():
    greeting = input('What is the greeting? ').lower().strip()

    print(greeting)

    def judge(decision):
        if decision.find('hello') == 0:
            return '$0'
        elif decision.find('h') == 0:
            return '$20'
        else:
            return '$100'

    print(judge(greeting))

main()