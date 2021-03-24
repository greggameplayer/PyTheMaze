from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.crocodile import Crocodile


class crocodileFactory(PersonnesFactory):

    def creerInstance(self):
        """
        Returns a new : class : rrocodile

        Args:
            self: (todo): write your description
        """
        return Crocodile()


PersonnesFactoryPrincipale.getInstance().registerFactory("crocodile", crocodileFactory())