from personnesFactory import PersonnesFactory, PersonnesFactoryPrincipale
from personnes.clown import Clown
import random


class clownFactory(PersonnesFactory):

    def __init__(self):
        """
        Initialize the _blagues.

        Args:
            self: (todo): write your description
        """
        self._blagues = ["", ""]

    def creerInstance(self):
        """
        Create a new : class : class : class : ~doctor.

        Args:
            self: (todo): write your description
        """
        return Clown(self._blagues)


PersonnesFactoryPrincipale.getInstance().registerFactory("clown", clownFactory())
