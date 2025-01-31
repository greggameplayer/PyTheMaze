import os
import sys
from importlib import import_module
from exceptions import AbstractMethodCallException
from joueur import Joueur
from labyrinthe.labyrinthe import Labyrinthe


class Action:

    def execute(self):
        """Abstraite"""
        raise AbstractMethodCallException(self.__class__.__name__, "execute")

    def description(self):
        """Abstraite"""
        raise AbstractMethodCallException(self.__class__.__name__, "description")

    def getCategories(self):
        return ["déplacement", "autre(s)"]


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
        return self.actions[cmd].execute()

    def descriptionCommande(self):
        for categorie in Action().getCategories():
            print(f"\n\n--     {categorie}     --\n")
            for key, val in self.actions.items():
                if val.getType() == categorie:
                    print('- ' + key + ' : ' + val.description())

    def afficherCommandesDispo(self):
        arrayCommandes = []
        for commande in self.actions.items():
            arrayCommandes.append(commande[0])
        commandes = "Commandes disponibles : "
        for i in range(0, len(arrayCommandes)):
            if i != len(arrayCommandes) - 1:
                commandes += arrayCommandes[i] + ", "
            else:
                commandes += arrayCommandes[i] + "."
        print(commandes)

    def jouer(self):
        j = Joueur.getInstance("👤", "X", 100)
        l = Labyrinthe.getInstance()
        j.printEnergie(sys.platform == "win32" and os.environ.get("WT_SESSION"))
        l.afficher()
        print()
        self.afficherCommandesDispo()
        while True:
            print("Que voulez vous faire ?")
            choix = input()
            try:
                self.executer(choix)
                break
            except KeyError:
                print("\nCommande inconnue, les seules commandes autorisées sont : ")
                self.descriptionCommande()
            except ValueError as e:
                print("\n" + e.__str__())
                self.afficherCommandesDispo()
