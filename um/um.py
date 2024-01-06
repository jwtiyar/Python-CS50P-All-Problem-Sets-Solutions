import re
import sys


def main():
    anjam = count(input("Text: "))
    print(anjam)


def count(s):
    test = re.findall(r"\bum\b", s, re.IGNORECASE)

    Numbers = 0
    for _ in test:
        Numbers += 1
    return Numbers


if __name__ == "__main__":
    main()
