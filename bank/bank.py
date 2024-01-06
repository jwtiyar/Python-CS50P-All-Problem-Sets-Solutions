def greeting_dollar():
    greet_message = input("Greeting: ")
    greet_message = greet_message.lower().strip()
    if greet_message == "hey":
        print("$20")
    elif greet_message.startswith("hello"):
        print("$0")
    elif greet_message.startswith("h"):
        print("$20")
    else:
        print("$100")

greeting_dollar()