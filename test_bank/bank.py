def main():
    greeting = input("Greeting: ")
    greeting = greeting.strip()
    encam = value(greeting)
    print(f"${encam}")
def value(greeting):
    greeting = greeting.lower()
    if greeting == "hey":
        return 20
    elif greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()