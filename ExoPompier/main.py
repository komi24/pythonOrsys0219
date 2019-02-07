# -*- coding: utf-8 -*-

"""
Faire une class Pompier
attribut : 
    position
    busy
methodes :
    se_deplacer( destination)
        deplace la position du pompier d'une case vers la destination
"""

from time import sleep
import os


class Pompier:
    def __init__(self, position):
        self.position =  position
        self.busy = 0
    def se_deplacer(self, destination, b):
        if self.busy > 0:
            self.busy -= 1
            return
        if destination[0] < self.position[0]:
            self.position[0] -= 1
        elif destination[0] > self.position[0]:
            self.position[0] += 1
        elif destination[1] < self.position[1]:
            self.position[1] -= 1
        elif destination[1] > self.position[1]:
            self.position[1] += 1
        else:
            self.busy = 5
            b.eteindre(self.position)
    def __repr__(self):
        return "Pompier : " + str(self.position)

import numpy as np
from tkinter import Tk, Canvas, PhotoImage

class Board:
    def __init__(self):
        self.size = [15,15]
        self.liste_pompier = [Pompier([4,3]),Pompier([5,11])]
        self.liste_feux = [[2,1], [5,3], [12,8], [2,8], [14,12]]
        self.fen = Tk()
        self.canvas = Canvas(self.fen, 
                             width=self.size[0]*32,
                             height=self.size[1]*32)
        self.canvas.pack()
        self.photo_pomp = PhotoImage(file="sm-pomp.gif")
        self.photo_feu = PhotoImage(file="sm-feu.gif")
        
        self.draw_everything()
        print("ok")
        self.fen.mainloop()

    def draw_everything(self):
        self.run()
        self.canvas.delete("all")
        for pompier in self.liste_pompier:
            self.canvas.create_image(pompier.position[0]*32 + 16,
                                     pompier.position[1]*32 + 16,
                                     image=self.photo_pomp)
        for feu in self.liste_feux:
            self.canvas.create_image(feu[0]*32 + 16,
                                     feu[1]*32 + 16,
                                     image=self.photo_feu)
        print(self.liste_feux)
        self.canvas.after(500, self.draw_everything)
        
    def eteindre(self, position):
        del self.liste_feux[self.liste_feux.index(position)]
    def feu_le_plus_proche(self, pompier):
        distance_min = np.linalg.norm(
                np.array(pompier.position) - np.array(self.liste_feux[0]), ord=1)
        result = self.liste_feux[0]
        """
        On suppose que le feu le plus proche est le premier feu
        On cherche dans la liste de feu si un feu est plus proche
        """
        for feu in self.liste_feux:
            distance = np.linalg.norm(
                np.array(pompier.position) - np.array(feu), ord=1)
            if distance < distance_min:
                """
                Si un feu est plus proche que celui de notre hypothèse
                On met a jour notre hypothèse
                """
                result = feu
                distance_min = distance
        return result
    
    def run(self):
        for pompier in self.liste_pompier:
            pompier.se_deplacer(
                    self.feu_le_plus_proche(pompier), self)
    
    def display(self):
        for i in range(self.size[0]):
            line = ""
            for j in range(self.size[1]):
                if [i,j] in self.liste_feux:
                    line += "x"
                elif [i,j] in [p.position for p in self.liste_pompier]:
                    line += "i"
                else:
                    line += " "
            print(line)
        

board = Board()
for i in range(40):
    board.run()
    os.system('cls')
    board.display()
    sleep(1)
    print(board.liste_pompier)
