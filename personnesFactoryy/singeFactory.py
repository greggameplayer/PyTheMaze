from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.singe import Singe


class singeFactory(PersonnesFactory):

    def creerInstance(self):
        """
        Returns a : class : ~doctor. cimlient } object.

        Args:
            self: (todo): write your description
        """
        return Singe()

PersonnesFactoryPrincipale.getInstance().registerFactory("singe", singeFactory())