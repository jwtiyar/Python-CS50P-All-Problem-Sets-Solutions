import csv
from sys import argv
import sys

if len(argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if argv[1][-4:] == ".csv" and argv[2][-4:] == ".csv":
        try:
            f = open(argv[1])
        except FileNotFoundError:
            sys.exit(f"Could not read {argv[1]}")
        else:
            students = []
            with f as file:
                reader = csv.DictReader(file)
                for row in reader:
                    table = row["name"]

                    table = table.replace(",", "")
                    table = table.split(" ")
                    last, first = table
                    students.append(
                        {"first": first, "last": last, "house": row["house"]}
                    )
            with open(argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for _ in range(len(students)):
                    writer.writerow(
                        {
                            "first": students[_]["first"],
                            "last": students[_]["last"],
                            "house": students[_]["house"],
                        }
                    )
    else:
        sys.exit("Not a CSV file")
