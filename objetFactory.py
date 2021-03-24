import os
from importlib import import_module


class ObjetFactory:

    def creerInstance(self):
        """
        Clears the current instance.

        Args:
            self: (todo): write your description
        """
        pass


class ObjetFactoryPrincipale:
    __instance = None

    @staticmethod
    def getInstance():
        """
        Return a : class : ~plexapi. baseipale. baseipaleipaleipaleipale.

        Args:
        """
        if ObjetFactoryPrincipale.__instance == None:
            ObjetFactoryPrincipale.__instance = ObjetFactoryPrincipale()
        return ObjetFactoryPrincipale.__instance

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
        for file in os.listdir(main_dir + "/objetsFactory"):
            if file.endswith(".py"):
                import_module("objetsFactory." + file[:-3])

    def creerObjet(self, objet):
        """
        Todo : doc of the given object.

        Args:
            self: (todo): write your description
            objet: (todo): write your description
        """
        return self._factories[objet].creerInstance()
