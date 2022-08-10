def main():
    import random

    x = random.randint(0, 10)
    print(x)

    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    for card in cards:
        print(card)

main()