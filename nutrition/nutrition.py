fruit_calories = {
    "Banana": "110",
    "Apple": "130",
    "Avocado": "50",
    "Cantaloupe": "50",
    "Watermelon": "80",
    "Tangerine": "50",
    "Sweet Cherries": "100",
    "Plums": "70",
    "Strawberries": "50",
    "Peach": "60",
    "Pear": "100",
    "Pineapple": "50",
    "Orange": "80",
    "Nectarine": "60",
    "Lime": "20",
    "Lemon": "15",
    "Kiwifruit": "90",
    "Honeydew Melon": "50",
    "Grapes": "90",
    "Grapefruit": "60",
}


def calories():
    fruits = input("Item: ")
    fruits = fruits.title()
    for f in fruit_calories:
        if fruits in f:
            print(fruit_calories[f])


calories()
