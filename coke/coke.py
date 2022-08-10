def main():
# Create a while loop that ask for Insert Coin
## Sums all Insert Coin until it is >= 50
## Then, return change owe and stop program
    def coin_check(money):
        if money == 5:
            return 5
        elif money == 10:
            return 10
        elif money == 25:
            return 25
        else:
            return 0

    counter = 0
    total = 0
    coke = 50

    while counter < 1:
        coin = int(input('Insert Coin: '))
        value = coin_check(coin)

        total += value
        if total >= 50:
            change = total - 50
            counter = 1
        else:
            due = 50 - total
            print('Amount Due:', due)

    print('Change Owed:', change)

main()