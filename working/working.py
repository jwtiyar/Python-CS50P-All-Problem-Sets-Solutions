import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.match(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s)
    if time:
        b_hour, b_minute, b_sign, a_hour, a_minute, a_sign = time.groups()
        if b_sign is None or b_minute is None or a_minute is None:
            b_minute = None or 0
            a_minute = None or 0
        b_hour = int(b_hour)
        a_hour = int(a_hour)
        a_minute = int(a_minute)
        b_minute = int(b_minute)

        if (a_hour or b_hour) > 23 or (a_minute or b_minute) > 59:
            raise ValueError()
        if b_hour == 12 and b_sign == "AM" and a_sign == "PM":
            return f"00:{b_minute:02} to {a_hour}:{a_minute:02}"
        elif a_hour == 12 and b_sign == "PM" and a_sign == "AM":
            return f"{b_hour:02}:{b_minute:02} to 00:{a_minute:02}"
        elif b_sign == "AM" and a_sign == "PM" != 12:
            b_hour += 0
            a_hour += 12

        elif b_sign == "PM" and a_sign == "AM" != 12:
            b_hour += 12
            a_hour += 0

        return f"{b_hour:02}:{b_minute:02} to {a_hour:02}:{a_minute:02}"

    raise ValueError()


if __name__ == "__main__":
    main()
