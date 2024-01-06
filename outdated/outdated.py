months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    date = input("Date: ")
    try:
        if "/" in date:
            mm, dd, yyyy = date.split("/")
        elif "," in date:
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")

            if mm in months[0:]:
                mm = months.index(mm) + 1

        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    except (KeyError, ValueError, NameError):
        pass

    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break
