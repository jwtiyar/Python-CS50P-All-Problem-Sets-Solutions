import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()
fa = random.choice(fonts)

if len(sys.argv) == 3:

    if sys.argv[2] in fonts and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        texstn = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        corepyt = figlet.renderText(texstn)
        print(corepyt)
    else:
        sys.exit("Invalid Usage")


elif len(sys.argv) == 1:
    texstn = input("Input: ")
    figlet.setFont(font=fa)
    corepyt = figlet.renderText(texstn)
    print(corepyt)
else:
    sys.exit("Invalid Usage")
