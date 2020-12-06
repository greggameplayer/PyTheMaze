from objetFactory import ObjetFactory, ObjetFactoryPrincipale
from objets.crane import Crane


class craneFactory(ObjetFactory):

    def creerInstance(self):
        return Crane.getInstance()


ObjetFactoryPrincipale.getInstance().registerFactory("crane", craneFactory())
