from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.sphinx import Sphinx


class sphinxFactory(PersonnesFactory):

    def creerInstance(self):
        """
        Return the : class : meth.

        Args:
            self: (todo): write your description
        """
        return Sphinx.getInstance()

PersonnesFactoryPrincipale.getInstance().registerFactory("sphinx", sphinxFactory())