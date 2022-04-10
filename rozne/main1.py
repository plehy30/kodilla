import sys
import string
import random
import os
import secrets
from colorama import init

init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
import time

choices_array = list()
os.system('cls')

cprint(figlet_format('RULETKA FEJDA'), 'blue')


def yesnochoice():
    while True:
        again = input("Jeszcze raz? (y/n):")
        if again in ['y', 'n']:
            return again
        print("Wpisz tak (y) lub nie (n).")


while True:
    try:

        choices = int(input("Ile chcesz mieć opcji?:"))
    except ValueError:
        print("Podaj numer")
        continue

    for i in range(choices):
        n = input("Wybór: ")
        choices_array.append(n)

    choice = secrets.choice(choices_array)

    print("Ostateczny wybór: " + choice)

    again = yesnochoice()

    if again == "y":
        continue
    elif again == "n":
        os.system("cls")
        break
