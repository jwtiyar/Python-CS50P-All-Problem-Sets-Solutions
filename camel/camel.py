camel = input("camelCase: ")
print("snake case: ")
for text in camel:
    if text.islower():
        print(text, end="")
    if text.isupper():
        print("_", text.lower(), end="", sep="")
print()
