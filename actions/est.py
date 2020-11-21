from action import Action
from joueur import Joueur


class Est(Action):
    joueur = Joueur.getInstance("X", 100)

    def execute(self):
        Est.joueur.avancerEst()
