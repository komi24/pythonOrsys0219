# -*- coding: utf-8 -*-

class Voiture:
    nb_voiture = 0
    def __init__(self, proprio, marque, vitesse_max=100):
        self.location = [0, 0]
        self.owner = proprio
        self.brand = marque
        self.vitesse_max = vitesse_max
        Voiture.nb_voiture += 1
        
    def se_deplacer(self, new_location):
        self.location = new_location
        
    def __str__(self):
        return "La voiture de " + self.owner
    
    def __gt__(self, other):
        return self.vitesse_max > other.vitesse_max
    
    def __eq__(self, other):
        return self.vitesse_max == other.vitesse_max

    def __ge__(self, other):
        return self.vitesse_max >= other.vitesse_max
    
    
ma_voiture = Voiture("Martin", "Maybach")
ta_voiture = Voiture("Marie", "Clio", 200)

print(ma_voiture.location)
ma_voiture.se_deplacer([2,5])
print(ma_voiture.location)
print(Voiture.nb_voiture)
print(ma_voiture)

print(ma_voiture >= ta_voiture)
