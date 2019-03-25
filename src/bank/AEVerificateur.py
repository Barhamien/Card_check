from BanqueCheck.src.bank.Luhalgo import Luhn
from IVerificateur import IVerificateur


class AEVerificateur(IVerificateur):
    def VerifierCarte(self):
        def VerifierCarte(self, cardNumber):
            if (len(cardNumber) == 17 & (cardNumber.startwith(39) | cardNumber.startwith(30))):
                Luhn(cardNumber)

            print("C'est une carte American Express")
            print("Carte invalide")

