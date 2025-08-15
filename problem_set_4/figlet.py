import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
    text = input("input: ")
    try:
        argument_1 = sys.argv[1]
        font_name = sys.argv[2]
    except:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
        random_font = figlet.renderText(text)
        print (random_font)
    else:
        if argument_1 == "-f" or argument_1 == "--font" and font_name in figlet.getFonts():
            figlet.setFont(font = font_name)
            chosen_font = figlet.renderText(text)
            print(chosen_font)
        else:
            sys.exit("invalid usage")

main()