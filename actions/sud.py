from action import Action
from joueur import Joueur


class Sud(Action):
    joueur = Joueur.getInstance("X", 100)

    def execute(self):
        Sud.joueur.avancerSud()
