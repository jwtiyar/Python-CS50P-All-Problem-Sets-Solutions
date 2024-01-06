def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    for shwen, char in enumerate(plate):
        if char.isdigit():
            char = int(char)
            break
    if (
        char != 0
        and len(plate) >= 2
        and plate.isalnum()
        and (plate.isalpha() or plate[-1].isdigit())
        and len(plate) < 7
        and plate[0:2].isalpha()
        and (plate[-2::].isdigit() or plate[-2::].isalpha())
    ):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
