from objetFactory import ObjetFactory,ObjetFactoryPrincipale
from objets.redbull import Redbull
import random

class redbullFactory(ObjetFactory):

    def creerInstance(self,joueur):
        expnb = random.randint(5, 10)
        return Redbull(expnb,joueur)

ObjetFactoryPrincipale.getInstance().registerFactory("redbull", redbullFactory())