from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.indiana import Indiana


class indianaFactory(PersonnesFactory):

    def creerInstance(self):
        """
        Return the : class instance.

        Args:
            self: (todo): write your description
        """
        return Indiana.getInstance()


PersonnesFactoryPrincipale.getInstance().registerFactory("indiana", indianaFactory())
