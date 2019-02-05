# -*- coding: utf-8 -*-

class Personne:
    def __init__(self, firstname, lastname):
        self.prenom = firstname
        self.nom = lastname
        self.age = 32
    
    def say_hello(self, name):
        print("Hello "+name)
    def say_hello_to(self, autre_personne):
        print("Hello "+autre_personne.prenom)

mon_voisin = Personne("Kevin", "Bertot")
mon_collegue = Personne("Jen", "Bertot")

print(mon_voisin.prenom)
mon_voisin.say_hello("John")
mon_voisin.say_hello_to(mon_collegue)