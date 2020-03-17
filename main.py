from random import *
from tkinter import*

meret = 555
ablak = Tk()
vaszon = Canvas(ablak, height=meret, width=meret)
vaszon.pack()
while True:
    szin = choice(['pink', 'orange', 'purple', 'yellow', 'blue'])
    x0 = randint(0, meret)
    y0 = randint(0, meret)
    d = randint(0, meret/5)
    vaszon.create_oval(x0, y0, x0 + d, y0 + d, fill=szin)
    ablak.update()
