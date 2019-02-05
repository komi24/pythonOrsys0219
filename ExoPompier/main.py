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
            b.eteindre()
    def __repr__(self):
        return "Pompier : " + str(self.position)

class Board:
    def __init__(self):
        self.size = [15,15]
        self.liste_pompier = [Pompier([4,3])]
        self.liste_feux = [[2,1], [5,3], [12,8]]
    def eteindre(self):
        del self.liste_feux[0]
    def run(self):
        self.liste_pompier[0].se_deplacer(self.liste_feux[0], self)
    
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
