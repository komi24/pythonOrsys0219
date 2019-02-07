from . import orm


class Personne(orm.Model):
	id = orm.Column(orm.Integer, primary_key=True)
	firstname = orm.Column(orm.String(100))
	lastname = orm.Column(orm.String(100))
	age = orm.Column(orm.Integer)

	def __init__(self, firstname, lastname, age):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age

