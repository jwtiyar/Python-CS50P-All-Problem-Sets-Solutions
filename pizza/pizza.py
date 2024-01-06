from tabulate import tabulate
import sys
import csv

test = sys.argv



def main():
    check_lines(test)
    table = get_menu()

    anjam = tabulate(table, headers="firstrow", tablefmt="grid")
    print(anjam)


def check_lines(test):
    # shwen = test[1]
    if len(test) >= 3:
        sys.exit("Too many command-line arguments")
    elif len(test) < 2:
        sys.exit("Too few command-line arguments")
    elif test[1][-3:] != "csv":
        sys.exit("Not a CSV file")
    else:
        pass
    return True


def get_menu():
    menu = []
    try:

        file = open(test[1], "r+")
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        reader = csv.reader(file)

        for row in reader:
            reader = csv.reader(file)
            print(row)
            menu.append(row)



        return menu


if __name__ == "__main__":
    main()
