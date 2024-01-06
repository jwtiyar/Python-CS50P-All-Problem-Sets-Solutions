def remove_vowel():
    text = input("Input: ")
    vowels = ["i", "I","O","o", "u", "U", "e", "E", "a", "A"]
    for char in text:
        if char in vowels:
            text = text.replace(char, "")
    print("Output:", text)
remove_vowel()