class DecouvertError(Exception):
    pass

class Compte:
    """
    attribut :
        proprio: Client
        solde:   int
    methodes :
        retrait(valeur)
        depot(valeur)
    """
    def __init__(self, proprio, solde):
        self.proprio = proprio
        self.solde = solde
        
    def retrait(self, valeur):
        if valeur > self.solde:
            raise DecouvertError()
        self.solde -= valeur
