from objetFactory import ObjetFactory, ObjetFactoryPrincipale
from objets.clef import Clef


class clefFactory(ObjetFactory):

    def creerInstance(self):
        """
        Return the currently active paleer.

        Args:
            self: (todo): write your description
        """
        return Clef()


ObjetFactoryPrincipale.getInstance().registerFactory("clef", clefFactory())
