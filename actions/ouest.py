from action import Action
from joueur import Joueur


class Ouest(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        Ouest.joueur.avancerOuest()
    def description(self):
        return "Permet de se déplacer vers l'Ouest"