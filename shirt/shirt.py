from sys import argv, exit
from PIL import Image, ImageOps
import os

extension = [".jpg", ".png"]

if len(argv) == 3:
    extension_1 = os.path.splitext(f"{argv[1]}")
    extension_2 = os.path.splitext(f"{argv[2]}")
    if (extension_1[1] and extension_2[1]) in extension:
        if extension_1[1] != extension_2[1]:
            exit("Input and Output have different extesnion")
    elif extension_2 not in extension:
        exit("Invalid Output")
    else:
        make_change(argv[1], argv[2])
elif len(argv) < 3:
    exit("Too few command-line arguments")

else:
    exit("Too many command-line arguments")


try:
    shirt = Image.open("shirt.png")
    with Image.open(argv[1]) as before:
        input = ImageOps.fit(before, shirt.size)
        input.paste(shirt, mask=shirt)
        input.save(argv[2])
except FileNotFoundError:
    exit("Input Does not exist")
