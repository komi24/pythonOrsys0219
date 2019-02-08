class Personne:
	def __init__(self):
		self.prenom = "Georges"

class ORM:
	def __init__(self):
		self.Model = Personne

une_personne = Personne()
print(une_personne.prenom)

orm = ORM()
print(orm.Model)

une_autre_personne = orm.Model()
print(une_autre_personne.prenom)



def ma_fonction(*params, **kwargs):
	for i in params:
		print(i)

	for key in kwargs:
		print("%s -> %s"%(key, kwargs[key]))


ma_fonction("okok", 4, personne="BOKOKOFKG", toto="okgokg")