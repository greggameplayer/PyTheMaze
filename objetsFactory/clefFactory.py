from objetFactory import ObjetFactory, ObjetFactoryPrincipale
from objets.clef import Clef


class clefFactory(ObjetFactory):

    def creerInstance(self):
        return Clef()


ObjetFactoryPrincipale.getInstance().registerFactory("clef", clefFactory())
