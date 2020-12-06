from action import Action
from joueur import Joueur


class Sud(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        Sud.joueur.avancerSud()
        Sud.joueur.perdreEnergie()

    def description(self):
        return "Permet de se déplacer vers le sud"

    def getType(self):
        return self.getCategories()[0]
