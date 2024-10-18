from pyfiglet import Figlet
from sys import argv, exit
from random import choice
#as david did in class
#from hitns

figlet = Figlet()

FigList = figlet.getFonts()

if len(argv) == 1:
    font_choice = choice(FigList)
    figlet.setFont(font=font_choice)
elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
    font_choice = argv[2]
    if font_choice not in FigList:
        exit("Invalid usage")
    figlet.setFont(font=font_choice)
else:
    exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
