import abc
class IVerificateur(object):
    __metaclass__=abc.ABCMeta
    pass
    @abc.abstractmethod
    def VerifierCarte(self):
        ''''implémentez moi'''''