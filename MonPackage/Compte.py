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
        