def main():
    time = input("What time is it? ")
    time = convert(time)
    # print(type(time))
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    time = time.replace(":", ".")
    # time = float(time)
    minutes = float(minutes)
    hours = float(hours)
    time = hours + minutes / 60
    time = float(time)
    # print(time)

    return time


if __name__ == "__main__":
    main()
