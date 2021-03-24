import os
from importlib import import_module


class PersonnesFactory:

    def creerInstance(self):
        """
        Clears the current instance.

        Args:
            self: (todo): write your description
        """
        pass


class PersonnesFactoryPrincipale:

    __instance = None

    @staticmethod
    def getInstance():
        """
        Return the instance of this class

        Args:
        """
        if __class__.__instance == None:  # Lazy loading
            __class__.__instance = __class__()
        return __class__.__instance


    def __init__(self):
        """
        Initialize the factories.

        Args:
            self: (todo): write your description
        """
        self._factories = {}

    def registerFactory(self, type, factory):
        """
        Registers a new factory.

        Args:
            self: (todo): write your description
            type: (todo): write your description
            factory: (todo): write your description
        """
        self._factories[type] = factory

    def loadFactoryPlugins(self):
        """
        Loads the modules from the module.

        Args:
            self: (todo): write your description
        """
        main_dir = os.path.dirname(__file__)
        for file in os.listdir(main_dir + "/personnesFactoryy"):
            if file.endswith(".py"):
                import_module("personnesFactoryy." + file[:-3])

    def creerPersonne(self, personne):
        """
        Returns the person object associated with the given person.

        Args:
            self: (todo): write your description
            personne: (todo): write your description
        """
        return self._factories[personne].creerInstance()
