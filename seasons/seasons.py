from datetime import date
import inflect
import sys

gorrer = inflect.engine()


def main():
    minutes = minutesDate()
    print(f"{ChangeToWords(minutes).capitalize()} minutes")


def minutesDate():
    try:
        birthdate = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid input.")
    kat = date.today()
    ledarkrdn = kat - birthdate
    chezh = ledarkrdn.total_seconds()
    inMinutes = round(chezh / 60)
    return inMinutes


def ChangeToWords(minutes):
    anjam = gorrer.number_to_words(minutes, andword="")
    return anjam


if __name__ == "__main__":
    main()
