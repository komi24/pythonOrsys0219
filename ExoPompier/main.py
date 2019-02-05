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
class Pompier:
    def __init__(self, position):
        self.position =  position
        self.busy = 0
    def se_delpacer(self, destination):
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