from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.sphinx import Sphinx


class sphinxFactory(PersonnesFactory):

    def creerInstance(self):
        return Sphinx.getInstance()

PersonnesFactoryPrincipale.getInstance().registerFactory("sphinx", sphinxFactory())