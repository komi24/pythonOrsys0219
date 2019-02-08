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
		self.compte = Compte("mickael", 100)
	def testRetraitSimple(self):
		self.compte.retrait(10)
		self.assertEqual(self.compte.solde, 90)
	def testRetraitDecouvert(self):
		with self.assertRaises(DecouvertError):
			self.compte.retrait(500)
	
