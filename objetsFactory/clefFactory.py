from objetFactory import ObjetFactory, ObjetFactoryPrincipale
from objets.clef import Clef

class clefFactory(ObjetFactory):

    def creerInstance(self,joueur):
        return Clef(joueur)

ObjetFactoryPrincipale.getInstance().registerFactory("clef", clefFactory())