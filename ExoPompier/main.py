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
from tkinter import *

class Board:
    def __init__(self):
        self.size = [15,15]
        self.liste_pompier = [Pompier([4,3]),Pompier([5,11])]
        self.liste_feux = [[2,1], [5,3], [12,8]]
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
