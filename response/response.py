import validators
def verify_email():
    response = input("What's your email address? ")
    check = validators.email(response)
    if check:
        print("Valid")
    else:
        print("Invalid")

verify_email()