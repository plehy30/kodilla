# Program to make a simple
# login screen

import tkinter as tk
fonty = ("Consolas",18,"bold")
root = tk.Tk()

root.geometry("600x400")


varX = tk.StringVar()
varY = tk.StringVar()


def licz():
    X = varX.get()

    # print("The name is : " + X)
    varY.set(f"X={X}")
    varX.set("")


labX = tk.Label(root, text='X=',font=fonty)
labY = tk.Label(root, textvariable=varY,font=fonty)
entX = tk.Entry(root, textvariable=varX,font=fonty)

btnLicz = tk.Button(root, text='Submit', command=licz,font=fonty)

labX.grid(row=0, column=0)
entX.grid(row=0, column=1)
labY.grid(row=1, column=1)
btnLicz.grid(row=2, column=1)

root.mainloop()
