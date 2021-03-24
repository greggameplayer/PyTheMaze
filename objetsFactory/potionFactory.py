from objetFactory import ObjetFactory,ObjetFactoryPrincipale
from objets.potion import Potion
import random


class potionFactory(ObjetFactory):

    def creerInstance(self):
        """
        Generate a cylinder.

        Args:
            self: (todo): write your description
        """
        expnb = random.randint(3, 15)
        return Potion(expnb)


ObjetFactoryPrincipale.getInstance().registerFactory("potion", potionFactory())