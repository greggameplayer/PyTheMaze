from action import Action
from joueur import Joueur
import random


class Regarder(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        """
        Executes the command.

        Args:
            self: (todo): write your description
        """
        case = Regarder.joueur.getCaseCourante()
        personnages = case.getPersonnages()
        objets = case.getObjets()
        if(len(personnages) == 0 and len(objets) == 0):
            print(random.choice([
                "Je vois une salle poussièreuse, sans rien de plus que quelques cailloux.",
                "Des toiles d'araignées un peu partout.",
                "C'est déseperement vide..."
            ]))
        else:
            print("Je vois :")
            for objet in objets:
                print(" - " + objet.description())
            for personnage in personnages:
                print(" - " + personnage.description())
        input()

    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return "Permet de regarder autour de soi"

    def getType(self):
        """
        Returns the type of the type

        Args:
            self: (todo): write your description
        """
        return self.getCategories()[1]
