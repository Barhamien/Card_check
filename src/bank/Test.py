from BanqueCheck.src.bank.Banque import Banque
from BanqueCheck.src.bank.IVerificateur import IVerificateur

if __name__ == "__main__":
    a = input ( "Saisir le numéro de la carte " )
    v=IVerificateur()
    b=Banque(v)
    b.verification(a)