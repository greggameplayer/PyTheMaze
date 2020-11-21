from action import Action
from joueur import Joueur


class Parler(Action):
    joueur = Joueur.getInstance("X", 100)

    def execute(self):
        print("Allo ? allo allo allo allo allo répète l'écho")
