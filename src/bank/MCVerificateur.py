from BanqueCheck.src.bank.Luhalgo import Luhn
from IVerificateur import IVerificateur


class MCVerificateur(IVerificateur):
    def VerifierCarte(self,cardNumber):
        if (len(cardNumber) == 16 & (cardNumber.startwith(41) | cardNumber.startwith(40))):
            Luhn(cardNumber)

        print("C'est une carte Mastercard")
        print("Carte invalide")

