# -*- coding: utf-8 -*-

"""
Un exemple de décorateur.
Nous modifierons le fonctionnement 
d'une fonction en la décorant.
"""


def premier_deco(f):
	"""
	Un décorateur qui ne fait presque rien.
	Il imprime 'hello' lors de la décoration
	"""
    print("Hello")
    return f


def mon_deco(f):
	"""
	Un décorateur qui modifie le comportement des fonctions.
	Il imprime 'hello' avant l'exécution de la fonction
	et 'Bye' à la fin.
	"""
    def new_func():
        print("Hello")
        f()
        print("Bye")

    return new_func
    

@mon_deco
def ma_fonction():
    print("Hello world")


ma_fonction()
ma_fonction()
