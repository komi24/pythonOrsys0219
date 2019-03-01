"""
Nous pouvons effectuer des tests en Docstring
Ou grace à unitTest. 
La première solution sert uniquement à donner des cas
d'utilisation simple (principaux use cases).
La deuxième solution doit assurer une bonne
couverture de code
"""

# def multiplier(a,b):
# 	"""
# 	:Example:
# 	>>> multiplier(2,2)
# 	4
# 	"""
# 	return a-b

# if __name__ == "__main__":
# 	import doctest
# 	doctest.testmod()


from unittest import TestCase
from MonPackage.Compte import Compte, DecouvertError

class CompteRetraitTest(TestCase):
	def setUp(self):
		"""
		Initialisation des éléments nécessaires pour
		procéder aux tests. Ici on va créer le compte
		sur lequel on testera différents retraits
		"""
		self.compte = Compte("mickael", 100)
	def testRetraitSimple(self):
		"""
		Un cas de retrait simple.
		Ce test sert à valider le use case principal
		"""
		self.compte.retrait(10)
		self.assertEqual(self.compte.solde, 90)
	def testRetraitDecouvert(self):
		"""
		Un cas de retrait en situation exceptionnelle.
		"""
		with self.assertRaises(DecouvertError):
			self.compte.retrait(500)
	
