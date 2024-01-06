def main():
    text = input("Input: ")
    # text = text.lower()
    encam = shorten(text)
    print("Output:", encam)


def shorten(text):
    vowels = ["i", "I","O","o", "u", "U", "e", "E", "a", "A"]
    for char in text:
        if char in vowels:
            text = text.replace(char, "")
            # text = text.lower()
    return text

if __name__ == "__main__":
    main()