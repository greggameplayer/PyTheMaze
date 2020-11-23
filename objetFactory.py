import os
from importlib import import_module


class ObjetFactory:

    def creerInstance(self,joueur):
        pass


class ObjetFactoryPrincipale:
    __instance = None

    @staticmethod
    def getInstance():
        if ObjetFactoryPrincipale.__instance == None:
            ObjetFactoryPrincipale.__instance = ObjetFactoryPrincipale()
        return ObjetFactoryPrincipale.__instance

    def __init__(self):
        self._factories = {}

    def registerFactory(self, type, factory):
        self._factories[type] = factory

    def loadFactoryPlugins(self):
        main_dir = os.path.dirname(__file__)
        for file in os.listdir(main_dir + "/objetsFactory"):
            if file.endswith(".py"):
                import_module("objetsFactory." + file[:-3])

    def creerObjet(self, objet,joueur):
        return self._factories[objet].creerInstance(joueur)
