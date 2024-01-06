import sys
import qrcode
import re
import pyshorteners
from art import *

intro = Art=text2art("QR Code and Url Shortener")
print(intro)
options = "1. Qr Code Generator\n2. Url Shortener"
print(options)
def main():
    texstn = input("Please chooose Url Shortner or QR Generator option: ")
    # User should select one option
    try:
        if texstn == "1":
            return qr_generator()
        elif texstn == "2":
            return make_short()
        else:
            raise ValueError  # raising this error will produce sys.exit with statment in the next step.

    except ValueError:
        sys.exit("Wrong selection")


def url_check():
    data = input("Enter Url Here: ")
    # checking url with regular expression
    encam = re.match(
        r"(http[s])?(://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        data,re.IGNORECASE
    )
    if encam:
        return encam.group()
    else:
        sys.exit("Invalid URL")


def qr_generator():
    # Box Specification
    qr = qrcode.QRCode(
        version=None,  # checked automatically if None
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # low error correction because it doesn't matter to our test case.
        box_size=20,
        border=1,
    )
    qr.add_data(url_check())  # bringing checked link
    qr.make(fit=True)
    img = qr.make_image(back_color=(10, 0, 0), fill_color=(236, 10, 10))
    img.save("QR code.png")

    # Do shortenening of the link
def make_short():
    link = url_check()
    # if link.startswith("http") :
    #     link.removeprefix("www")
    shorter = pyshorteners.Shortener(api_key='0b89beac8801d5b3a5ae2fed4051cad0b6f430e3')
    shortening = shorter.bitly.short(link)
    print(shortening)
    # else:
    #     print("Oops, Please add Http protocol to the link")

if __name__ == "__main__":
    main()
