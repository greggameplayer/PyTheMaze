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
        """
        Return a list of categories.

        Args:
            self: (todo): write your description
        """
        return ["déplacement", "autre(s)"]


class ActionManager:
    __instance = None

    @staticmethod
    def getInstance():
        """
        Return a : class : class : ~django. base. base. base. base.

        Args:
        """
        if ActionManager.__instance is None:
            ActionManager.__instance = ActionManager()
        return ActionManager.__instance

    def __init__(self):
        """
        Initialize actions

        Args:
            self: (todo): write your description
        """
        self.actions = {}

    def registerCommand(self, cmd, instanceAction):
        """
        Registers an instance command.

        Args:
            self: (todo): write your description
            cmd: (str): write your description
            instanceAction: (todo): write your description
        """
        self.actions[cmd] = instanceAction

    def loadActionPlugins(self):
        """ Charge dynamiquement tous les modules présents dans le dossier actions"""
        main_dir = os.path.dirname(__file__)
        for file in os.listdir(main_dir + "/actionsCommand"):
            if file.endswith(".py"):
                import_module("actionsCommand." + file[:-3])

    def executer(self, cmd):
        """
        Execute a command.

        Args:
            self: (todo): write your description
            cmd: (str): write your description
        """
        return self.actions[cmd].execute()

    def descriptionCommande(self):
        """
        Print the description

        Args:
            self: (todo): write your description
        """
        for categorie in Action().getCategories():
            print(f"\n\n--     {categorie}     --\n")
            for key, val in self.actions.items():
                if val.getType() == categorie:
                    print('- ' + key + ' : ' + val.description())

    def afficherCommandesDispo(self):
        """
        Afficherherhericheres for this toolbar

        Args:
            self: (todo): write your description
        """
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
        """
        Execute jouer

        Args:
            self: (todo): write your description
        """
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
