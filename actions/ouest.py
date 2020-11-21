from action import Action
from joueur import Joueur


class Ouest(Action):
    joueur = Joueur.getInstance("X", 100)

    def execute(self):
        Ouest.joueur.avancerOuest()