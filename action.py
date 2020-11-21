import os 
from importlib import import_module

class Action:

    def execute(self, param):
        """Abstraite"""

    def info(self):
        """donne les informations de l'action"""

    def help(self):
        """ donne une description longue de la commande """
        pass

class ActionManager:

    __instance = None

    @staticmethod
    def getInstance():
        if ActionManager.__instance == None:
            ActionManager.__instance = ActionManager()
        return ActionManager.__instance

    def __init__(self):
        self.actions = {}

    def registerCommand(self, cmd, instanceAction):
        self.actions[cmd] = instanceAction

    def loadActionPlugins(self):
        """ Charge dynamiquement tous les modules présents dans le dossier actions"""
        main_dir = os.path.dirname(__file__)
        for file in os.listdir(main_dir + "/actions"):
            if file.endswith(".py"):
                import_module("actions." + file[:-3])  

    def executerEntreeUtilisateur(self, entreeUtilisateur):
        try:
            [action, param] = entreeUtilisateur.split(" ", 1)
        except ValueError:
            # Si ValueError, le split ne renvoie qu'un seul élément
            action = entreeUtilisateur
            param = ""
        self.executer(action, param)    

    def executer(self, cmd, param):
        try:
            self.actions[cmd].execute(param)
        except KeyError:
            print("Commande inconnue")

    def afficherCommandesDispo(self):
        for key, val in self.actions.items():
            print(key + ": " + val.info())
