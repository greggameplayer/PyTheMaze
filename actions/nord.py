from action import Action
from joueur import Joueur


class Nord(Action):
    joueur = Joueur.getInstance("X", 100)

    def execute(self):
        Nord.joueur.avancerNord()
