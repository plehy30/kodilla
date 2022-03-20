# Program oblicza nominały potrzebne do wypłaty podanej kwoty
import sys
import tkinter as tk
from decimal import *

# przygotowanie okna i fontów
okno = tk.Tk()
okno.geometry("700x800")
okno.option_add("*font", "arial 20 normal")  # domyślny font aplikacji
fonty = ("Consolas", 20, "normal")          # font lokalny

# zmienne programu
nominal = ('500', '200', '100',
           '50', '20', '10',
           '5', '2', '1',
           '0.5', '0.2', '0.1',
           '0.05', '0.02', '0.01')
ile = []
varX = tk.StringVar()


# funkcja obliczania nominałów dla podanej kwoty
def licz():
    global ile
    x = Decimal(varX.get())
    wyniki.insert(tk.INSERT, f"kwota = {x:.2f}\n")
    r = x
    wnom = "\n"
    for nom in nominal:
        dnom = Decimal(nom)
        n = 0
        while r >= dnom:
            r -= dnom
            n += 1
            wnom += f"{nom:5} "
        ile.append(n)
        wyniki.insert(tk.INSERT, f"{nom:8}zł : {n}  {r}\n")

    wyniki.insert(tk.INSERT, wnom)
#    wyniki.insert(tk.INSERT, f"\n\nile = {ile}\n")


# kasowanie i przygotowanie interfejsu do następnych obliczeń
def kasuj():
    global ile
    kwota.delete(0, tk.END)
    wyniki.delete("1.0", tk.END)
    ile = []


# wyjście z programu
def koniec():
    sys.exit(0)


# Utworzenie graficznego interfejsu programu
f1 = tk.Frame(okno)
l1 = tk.Label(f1, text='kwota=')
kwota = tk.Entry(f1, textvariable=varX, font=fonty)
f1.pack(fill=tk.X)
l1.pack(side=tk.LEFT)
kwota.pack(side=tk.LEFT)

f2 = tk.Frame(okno)
bLicz = tk.Button(f2, text='Oblicz', command=licz)
bKasuj = tk.Button(f2, text='Kasuj', command=kasuj)
bStop = tk.Button(f2, text='Zamknij', command=koniec)
f2.pack(fill=tk.X)
bLicz.pack(side=tk.LEFT)
bKasuj.pack(side=tk.LEFT)
bStop.pack(side=tk.LEFT)

f3 = tk.Frame(okno)
wyniki = tk.Text(f3, font=fonty)
f3.pack(fill=tk.X)
wyniki.pack(side=tk.LEFT, fill=tk.BOTH)

# start pętli obsługi komunikatów
okno.mainloop()
