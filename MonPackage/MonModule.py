# -*- coding: utf-8 -*-
from . import nb_phrase

def dire_bonjour(name):
    nb_phrase['count'] += 1
    print("Bonjour " + name)
    

def say_hello(name, lng="En"):
    """
    lng par défaut en En
    En fonction de lng, print Bonjour nam, Hello name etc. 
    """
    nb_phrase['count'] += 1
    phrase = {
            "En": "Hello "+name,
            "Fr": "Bonjour "+name,
            "Pt": "Bom dia "+name,
            "Es": "Hola "+name,
            "Zh": "Nin Hao "+name,
            "Cr": "Sa ou fè "+name
            }
    print(phrase[lng])
#    if lng == "En":
#        print("Hello "+name)
#        return
#    if lng == "Fr":
#        print("Bonjour "+name)
#        return
#    if lng == "Es":
#        print("Hola "+name)
#        return
#    if lng == "Pt":
#        print("Bom dia "+name)
#        return
#    if lng == "Zh":
#        print("Ni hao "+name)
#        return
#    if lng == "Cr":
#        print("Sa ou fè "+name)
#        return

if __name__ == "__main__":
    say_hello("Baptiste")