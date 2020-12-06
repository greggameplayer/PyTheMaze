from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.indiana import Indiana


class indianaFactory(PersonnesFactory):

    def creerInstance(self):
        return Indiana.getInstance()


PersonnesFactoryPrincipale.getInstance().registerFactory("indiana", indianaFactory())
