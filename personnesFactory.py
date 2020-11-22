import os
from importlib import import_module

class PersonnesFactory:

    def creerInstance(self):
        pass

class PersonnesFactoryPrincipale:

    __instance = None

    @staticmethod
    def getInstance():
        if __class__.__instance == None:  # Lazy loading
            __class__.__instance = __class__()
        return __class__.__instance


    def __init__(self):
        self._factories = {}

    def registerFactory(self, type, factory):
        self._factories[type] = factory

    def loadFactoryPlugins(self):
        main_dir = os.path.dirname(__file__)
        for file in os.listdir(main_dir + "/personnesFactoryy"):
            if file.endswith(".py"):
                import_module("personnesFactoryy." + file[:-3])

    def creerPersonne(self, personne):
        return self._factories[personne].creerInstance()