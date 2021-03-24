from objetFactory import ObjetFactory,ObjetFactoryPrincipale
from objets.redbull import Redbull
import random

class redbullFactory(ObjetFactory):

    def creerInstance(self):
        """
        Return a new instance of this : attbull.

        Args:
            self: (todo): write your description
        """
        return Redbull()

ObjetFactoryPrincipale.getInstance().registerFactory("redbull", redbullFactory())