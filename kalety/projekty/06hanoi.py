# Program oblicza nominały potrzebne do wypłaty podanej kwoty
import sys
import tkinter as tk

fonty = ("Consolas", 16, "normal")
okno = tk.Tk()

varN = tk.StringVar(value="5")

def hanoi(n, z, na, pom):
    if n == 1:
        wyniki.insert(tk.INSERT, f"{z} => {na}\n")
    else:
        hanoi(n - 1, z, pom, na)
        wyniki.insert(tk.INSERT, f"{z} => {na}\n")
        hanoi(n - 1, pom, na, z)


def hanoistart():
    wyniki.delete("1.0", tk.END)
    n = int(varN.get())
    hanoi(n, 'A', 'B', 'C')


def koniec():
    sys.exit(0)


f1 = tk.Frame(okno)
l1 = tk.Label(f1, text='n=', font=fonty)
nn = tk.Entry(f1, textvariable=varN, font=fonty)
f1.pack(fill=tk.X)
l1.pack(side=tk.LEFT)
nn.pack(side=tk.LEFT)

f2 = tk.Frame(okno)
bLicz = tk.Button(f2, text='Oblicz', command=hanoistart, font=fonty)
bStop = tk.Button(f2, text='Zamknij', command=koniec, font=fonty)
f2.pack(fill=tk.X)
bLicz.pack(side=tk.LEFT)
bStop.pack(side=tk.LEFT)

f3 = tk.Frame(okno)
wyniki = tk.Text(f3, font=fonty)
f3.pack(fill=tk.X)
wyniki.pack(side=tk.LEFT, fill=tk.BOTH)

okno.mainloop()
