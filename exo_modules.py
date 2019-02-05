# -*- coding: utf-8 -*-

#from MonPackage.MonModule import dire_bonjour
#
#dire_bonjour("Martin")
#dire_bonjour("Eloise")
#dire_bonjour("Justine")
#dire_bonjour("Robert")

#from MonPackage import MonModule 
#
#MonModule.dire_bonjour("Martin")
#MonModule.dire_bonjour("Eloise")
#MonModule.dire_bonjour("Justine")
#MonModule.dire_bonjour("Robert")

""" 
Import `dire_bonjour` directement depuis mon package
Car on l'a rajouté au namespace 
du package (dans __init__.py)
"""
from MonPackage import dire_bonjour, nb_phrase
from MonPackage.Conversation import converser
from MonPackage.MonModule import say_hello

dire_bonjour("Martin")
dire_bonjour("Eloise")
dire_bonjour("Justine")
dire_bonjour("Robert")
print(nb_phrase)
converser("Arthur", "Elise")
print(nb_phrase)
say_hello("Mickael", "Cr")
say_hello("Maria", "Zh")
say_hello("Martin")
say_hello("Mylenne", "Pt")
