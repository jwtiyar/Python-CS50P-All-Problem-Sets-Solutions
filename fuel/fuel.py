def main():
    while True:
        try:
            encam = get_fraction()
            if encam >= 0.0 and encam <= 0.1:
                print("E")
            elif encam >= 0.9 and encam <= 1.0:
                print("F")
            elif encam < 0.9 and encam > 0.1:
                x = round(encam * 100)
                print(f"{x}%")

        except ZeroDivisionError:
            pass
        else:
            break


def get_fraction():
    while True:
        try:
            human = input("Fraction: ").split("/")
            x, y = human
            x = int(x)
            y = int(y)
            if x > y:
                continue
        except ValueError:
            pass

        else:
            return x / y


main()
