import sys

def lines():
    test = sys.argv
    shwen = test[1]
    if len(test) >= 3:
        sys.exit("Too many")
    elif len(test) <= 1:
        sys.exit("Too few")
    elif shwen[-2:] != "py":
        sys.exit("Not a python file")
    else:
        pass

    try:
        with open(test[1], "r") as file:
            file = file.readlines()
            count = len(file)
            for line in file:
                hell = line.lstrip()

                if hell.startswith("#") or hell.strip() == "":
                    count -= 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


lines()