# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas, PhotoImage
from time import sleep

fen = Tk()

size = (15,15)
img_size = (32, 32)
photo = PhotoImage(file="sm-feu.gif")

photo_pompier = PhotoImage(file="sm-pomp.gif")

canvas = Canvas(
        fen, 
        width=img_size[0] * size[0], 
        height=img_size[1] * size[1])

canvas.pack()

i=0
def next_move():
    global i
    canvas.delete("all")
    canvas.create_image(img_size[0]//2, img_size[1]//2, image=photo)
    canvas.create_image(i*img_size[0]+img_size[0]//2,
                        i*img_size[1]+img_size[1]//2, 
                        image=photo_pompier)
    i+=1
    if i < 12:
        canvas.after(500,next_move)
    
canvas.after(500, next_move)


fen.mainloop()
