import logging


def dodawanie(x, y):
    return int(x) + int(y)


def odejmowanie(x, y):
    return int(x) - int(y)


def mnozenie(x, y):
    return int(x) * int(y)


def dzielenie(x, y):
    return int(x) / int(y)


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
        operator = input('Podaj znak działania: ')
        if operator == '+':
            logging.info("Teraz dodaję")
            print(f'wynik dodawania {x} i {y} wynosi {dodawanie(x, y)}')
            pytanie = int(input("Liczymy dalej? Jeżeli tak to naciśnij jakąś cyfrę, a jeżeli nie to naciśnij 0"))
            if pytanie == 0:
                break
            else:
                continue
        elif operator == '-':
            print(f'wynik odejmowania {x} i {y} wynosi {odejmowanie(x, y)}')
            pytanie = int(input("Liczymy dalej? Jeżeli tak to naciśnij jakąś cyfrę, a jeżeli nie to naciśnij 0"))
            if pytanie == 0:
                break
            else:
                continue
        elif operator == '*':
            print(f'wynik mnożenia {x} i {y} wynosi {mnozenie(x, y)}')
            pytanie = int(input("Liczymy dalej? Jeżeli tak to naciśnij jakąś cyfrę, a jeżeli nie to naciśnij 0"))
            if pytanie == 0:
                break
            else:
                continue
        elif operator == '/':
            print(f'wynik dzielenia {x} i {y} wynosi {dzielenie(x, y)}')
            pytanie = int(input("Liczymy dalej? Jeżeli tak to naciśnij jakąś cyfrę, a jeżeli nie to naciśnij 0"))
            if pytanie == 0:
                break
            else:
                continue
        else:
            print('Zły znak')
    else:
        break

print('Koniec')
