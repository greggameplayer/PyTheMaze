from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.indiana import Indiana


class indianaFactory(PersonnesFactory):

    def creerInstance(self):
        return indiana()

PersonnesFactoryPrincipale.getInstance().registerFactory("indiana", indianaFactory())