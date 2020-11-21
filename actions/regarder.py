from action import Action, ActionManager
from joueur import Joueur
import random


class Regarder(Action):
    joueur = Joueur.getInstance("X", 100)

    def _init_(self, letter):
        self.case = Regarder.joueur.getCaseCourante()
        self.personnages = self.case.getPersonnages()
        self.objets = self.case.getObjets()
        self.execute()

    def execute(self, param=0):
        if (len(self.personnages) == 0 and len(self.objets) == 0):
            print(random.choice([
                "Je vois une salle poussièreuse, sans rien de plus que quelques cailloux.",
                "Des toiles d'araignées un peu partout.",
                "C'ets déseperement vide..."
            ]))
        else:
            print("Je vois :")
            for objet in self.objets:
                print(" - " + objet.description())
            for personnage in self.personnages:
                print(" - " + personnage.description())

    def info(self):
        pass

    def help(self):
        pass
