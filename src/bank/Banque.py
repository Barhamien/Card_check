from BanqueCheck.src.bank.AEVerificateur import AEVerificateur
class Banque:
    def __init__(self, Iverifie):
        self.Iverifie = Iverifie

    def getNum(self):
        return self.Iverifie

    def setNum(self, Iverifi):
        self.Iverifie = Iverifi

    # class
    def verification(self, Iverifie):
        self.Iverifie.VerifierCarte()

