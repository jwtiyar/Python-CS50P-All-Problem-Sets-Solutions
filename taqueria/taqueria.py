menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


#  = menu.keys()
try:
    while True:
        sum = 0

        for item in menu.keys():
            try:
                item = input("item: ")
            except KeyError:
                print("\n")
                pass

            item = item.title()
            if item in menu.keys():
                sum = sum + menu[item]
                print(f"Total: ${sum:.2f}")
except EOFError:
    print("\n")
    pass

