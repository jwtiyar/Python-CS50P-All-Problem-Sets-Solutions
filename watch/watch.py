import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    clean = re.search(r"src=\"(?:https?://)?(?:www\.)?youtube\.com/embed/(.+?)\"", s)
    if clean:
        return f"https://youtu.be/{clean.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
