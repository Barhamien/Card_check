from BanqueCheck.src.bank.Luhalgo import Luhn
from IVerificateur import IVerificateur


class VisaVerificateur(IVerificateur):
    def VerifierCarte(self, cardNumber):
        if(len(cardNumber)==15 & (cardNumber.startwith(14) | cardNumber.startwith(14))):
            Luhn(cardNumber)


        print("C'est une carte Visa")