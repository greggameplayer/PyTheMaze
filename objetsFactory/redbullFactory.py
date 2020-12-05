from objetFactory import ObjetFactory,ObjetFactoryPrincipale
from objets.redbull import Redbull
import random

class redbullFactory(ObjetFactory):

    def creerInstance(self):
        return Redbull()

ObjetFactoryPrincipale.getInstance().registerFactory("redbull", redbullFactory())