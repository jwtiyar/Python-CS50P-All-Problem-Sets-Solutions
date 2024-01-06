grocery = []
grocery = sorted(grocery)
try:
    while True:
        item = input().upper().strip()
        grocery.append(item)

except EOFError:
    for item in sorted(set(grocery)):
        print(grocery.count(item), item)
except KeyError:
    pass
