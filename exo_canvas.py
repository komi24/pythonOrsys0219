# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas, PhotoImage


fen = Tk()

size = (5,5)
img_size = (160, 160)
photo = PhotoImage(file="feu.gif")
canvas = Canvas(fen, width=img_size[0] * size[0], height=img_size[1] * size[1])
canvas.pack()

canvas.create_image(img_size[0]//2, img_size[1]//2, image=photo)

fen.mainloop()