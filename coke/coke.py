def coin():
    total = 0
    amount = 50
    while amount > 0:
        print("Amount Due:", amount)
        coins = int(input("Insert Coin: "))
        if coins in [5, 10, 25]:
            amount = amount - coins
            total = total + coins
            print("Change Owed:", total - 50)


coin()
