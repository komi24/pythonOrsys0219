# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, Frame
from tkinter import TOP, LEFT, BOTTOM, RIGHT
from itertools import product

fen = Tk()

label = Label(fen, text="0", height=3)
label.pack(expand=True, fill="both")

mainframe = Frame(fen)
mainframe.pack(side=LEFT)

for op in ["+","-","*","/"]:
    Button(fen, text=op, width=6, height=2).pack()

frame = Frame(mainframe)
frame.pack()

bouton_zero = Button(mainframe, text="0", height=2)
bouton_zero.pack(expand=True, fill='both')
#label = Label(fen, text="Bonjour tout le monde !", padx=40, pady=10)
#label.pack(side=LEFT)
#
#btn = Button(fen, text="Mon Bouton")
#btn.pack(side=BOTTOM)
#
#btn2 = Button(fen, text="Mon deuxieme Bouton")
#btn2.pack()

for i,j in product(range(3), range(3)):
    btn = Button(frame, text=str(i*3+j+1), width=6, height=2)
    btn.grid(row=2-i, column=j)

fen.mainloop()