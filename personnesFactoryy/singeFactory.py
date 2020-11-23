from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.singe import Singe


class singeFactory(PersonnesFactory):

    def creerInstance(self):
        return Singe()

PersonnesFactoryPrincipale.getInstance().registerFactory("singe", singeFactory())