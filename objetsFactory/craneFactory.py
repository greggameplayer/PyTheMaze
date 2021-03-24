from objetFactory import ObjetFactory, ObjetFactoryPrincipale
from objets.crane import Crane


class craneFactory(ObjetFactory):

    def creerInstance(self):
        """
        Return the current : classane.

        Args:
            self: (todo): write your description
        """
        return Crane.getInstance()


ObjetFactoryPrincipale.getInstance().registerFactory("crane", craneFactory())
