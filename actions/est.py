from action import Action
from joueur import Joueur


class Est(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        Est.joueur.avancerEst()
        Est.joueur.perdreEnergie()

    def description(self):
        return "Permet de se déplacer vers l'Est"

    def getType(self):
        return self.getCategories()[0]