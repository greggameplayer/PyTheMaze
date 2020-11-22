import os
from importlib import import_module


class Action:

    def execute(self):
        """Abstraite"""

    def description(self):
        """Abstraite"""

class ActionManager:
    __instance = None

    @staticmethod
    def getInstance():
        if ActionManager.__instance is None:
            ActionManager.__instance = ActionManager()
        return ActionManager.__instance

    def __init__(self):
        self.actions = {}

    def registerCommand(self, cmd, instanceAction):
        self.actions[cmd] = instanceAction

    def loadActionPlugins(self):
        """ Charge dynamiquement tous les modules présents dans le dossier actions"""
        main_dir = os.path.dirname(__file__)
        for file in os.listdir(main_dir + "/actionsCommand"):
            if file.endswith(".py"):
                import_module("actionsCommand." + file[:-3])

    def executer(self, cmd):
        try:
            return self.actions[cmd].execute()
        except:
            print("\n\nCommande inconnue, les seules commandes autorisées sont : ")
            self.descriptionCommande()

    def descriptionCommande(self):
        for key, val in self.actions.items():
            print('-' + key +' : '+ val.description())
        input()

    def afficherCommandesDispo(self):
        print("Commandes disponibles : ")
        for commande in self.actions.items():
            print(commande[0], end = ", ")