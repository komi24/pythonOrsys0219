# -*- coding: utf-8 -*-

"""
Introduction à Tkinter pour créer des fenêtres.
"""


from tkinter import Tk, Label, Button, Frame
from tkinter import TOP, LEFT, BOTTOM, RIGHT, StringVar
from itertools import product


class MonBouton(Button):
    def __init__(self, root, text="", width="", height="", value=""):
        Button.__init__(self, root, text=text, width=width, height=height)
        self.value = value


fen = Tk()

ma_chaine = StringVar()
ma_chaine.set("0")


label = Label(fen, textvariable=ma_chaine, height=3)
label.pack(expand=True, fill="both")

mainframe = Frame(fen)
mainframe.pack(side=LEFT)

for op in ["+","-","*","/"]:
    Button(fen, text=op, width=6, height=2).pack()

frame = Frame(mainframe)
frame.pack()

def ma_fonction(event):
    print(dir(event.widget))
    print("Hello")
    ma_chaine.set(event.widget.value)

bouton_zero = Button(mainframe, text="0", height=2, command=ma_fonction)
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
    btn = MonBouton(frame, text=str(i*3+j+1), width=6, height=2, value=str(i*3+j+1))
    btn.bind('<Button-1>', ma_fonction)
    btn.grid(row=2-i, column=j)

fen.mainloop()