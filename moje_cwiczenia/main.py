import sys;
import string;
import random;
import os;
import secrets;
from colorama import init

init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
import time

choices_array = list()
os.system('cls')

cprint(figlet_format('RULETKA FEJDA'), 'blue')

try:

    choices = input("Ile chcesz mieć opcji?:")

    for i in range(int(choices)):
        n = input("Wybór: ")
        choices_array.append(n)

    choice = secrets.choice(choices_array)

    print("Ostateczny wybór: " + choice)
    again = input("Jeszcze raz? (y/n):")
    if again == "y":
        os.system("python ./main.py")
    elif again == "n":
        os.system("cls")
    else:
        print("Wpisz tak (y) lub nie (n).")

except ValueError:
    print("Musisz wprowadzić numer!")
    time.sleep(1)
    os.system("python ./main.py")
