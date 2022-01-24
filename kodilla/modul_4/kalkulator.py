import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# def dodawanie(x, y):
#     return int(x) + int(y)
#
#
# def odejmowanie(x, y):
#     return int(x) - int(y)
#
#
# def mnozenie(x, y):
#     return int(x) * int(y)
#
#
# def dzielenie(x, y):
#     return int(x) / int(y)
def operacja(op, x, y):
    if op == "+": return x + y
    logger.debug('odejmujemy dwie liczby')
    if op == "-": return x - y
    logger.debug('mnożymy dwie liczby')
    if op == "*": return x * y
    logger.debug('dzielimy dwie liczby')
    if op == "/": return x / y


def logowanie():
    if op == "+":
        logger.debug(f'dodajemy dwie liczby {x} {y}')


powitanie = input('Witaj! Czy chcesz liczyć? Jeżeli tak to naciśnij T, jeżeli nie to dowolny klawisz. ')
powitanie = powitanie.upper()
while True:
    if powitanie == 'T':
        x = input('Podaj pierwszą liczbę: ')
        while not x.isdigit():
            x = input('Podaj pierwszą liczbę: ')
        y = input('Podaj drugą liczbę: ')
        while not y.isdigit():
            y = input('Podaj druga liczbę liczbę: ')
        x = int(x)
        y = int(y)
        while True:
            operator = input('Podaj znak działania: ')
            if operator == "": continue
            op = operator[0]
            if op not in '+-*/': continue
            break
        logowanie()
        w = operacja(op, x, y)
        print(f"{x} {op} {y} = {w}")
        # if operator[0] == '+':
        #     logging.info("Teraz dodaję")
        #     print(f'wynik dodawania {x} i {y} wynosi {dodawanie(x, y)}')
        # elif operator[0] == '-':
        #     print(f'wynik odejmowania {x} i {y} wynosi {odejmowanie(x, y)}')
        # elif operator[0] == '*':
        #     print(f'wynik mnożenia {x} i {y} wynosi {mnozenie(x, y)}')
        # elif operator[0] == '/':
        #     print(f'wynik dzielenia {x} i {y} wynosi {dzielenie(x, y)}')
        # break
        pytanie = input("Liczymy dalej? Jeżeli tak to naciśnij jakąś cyfrę, a jeżeli nie to naciśnij 0")
        if pytanie == "0":
            break
        else:
            continue

print('Koniec')
