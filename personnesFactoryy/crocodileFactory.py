from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.crocodile import Crocodile


class crocodileFactory(PersonnesFactory):

    def creerInstance(self):
        return Crocodile()


PersonnesFactoryPrincipale.getInstance().registerFactory("crocodile", crocodileFactory())