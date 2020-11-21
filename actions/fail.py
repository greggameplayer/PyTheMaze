from action import Action
from joueur import Joueur


class Fail(Action):
    joueur = Joueur.getInstance("X", 100)

    def execute(self):
        print("Moi pas comprendre...")
        print("Mon vocabulaire est limité  à n, s, e, o, regarder, ramasser, sac et parler.")
        input()