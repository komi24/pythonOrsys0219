class Personne:
    """
    Classe Personne representant une personne avec un 
    nom et un prenom.
    Cette personne peut se presenter et dire bonjour
    attributs : 
        - nom
        - prenom
        - age
    methodes :
        - dire_bonjour : dit bonjour à une autre personne
        - se_presenter : se presente en fournissant son nom et son prenom
    """
    def __init__(self, prenom, nom, age=19):
        """
        :param prenom: str
        :param nom:   str
        :param age:   int
        """
        assert isinstance(prenom, str)
        assert isinstance(nom, str)
        assert isinstance(age, int)
        self.prenom = prenom
        self.nom = nom
        self.age = age
        
    def dire_bonjour(self, autre_personne):
        """
        Affiche : 'Bonjour [le nom de l'autre personne]'
        """
        assert isinstance(autre_personne, Personne)
        assert self.age >= 18, "Trop jeune pour dire bonjour"
        print("Bonjour " + autre_personne.prenom)
    
    def se_presenter(self):
        """
        Affiche : Je m'appelle [prenom] [nom] et j'ai [age] ans
        """
        print("Je m'appelle %s %s et j'ai %d ans"%
              (self.prenom, self.nom, self.age))

class Client(Personne):
    def __init__(self, prenom, nom, age=18, solde=4500):
        """
        On rapelle le constructeur de Personne
        dans la classe fille Client afin d'initialiser
        prenom, nom et age
        """ 
        Personne.__init__(self, prenom, nom, age)
        self.compte = Compte(self, solde)
        
    def say_hello(self):
        print("Hello")