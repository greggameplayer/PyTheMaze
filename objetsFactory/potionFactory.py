from objetFactory import ObjetFactory,ObjetFactoryPrincipale
from objets.potion import Potion
import random

class potionFactory(ObjetFactory):

    def creerInstance(self, joueur=""):
        expnb = random.randint(5, 10)
        return Potion(expnb)

ObjetFactoryPrincipale.getInstance().registerFactory("potion", potionFactory())