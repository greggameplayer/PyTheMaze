from personnesFactory import PersonnesFactory, PersonnesFactoryPrincipale
from personnes.clown import Clown
import random


class clownFactory(PersonnesFactory):

    def __init__(self):
        self._blagues = ["", ""]

    def creerInstance(self):
        return Clown(self._blagues)


PersonnesFactoryPrincipale.getInstance().registerFactory("clown", clownFactory())
