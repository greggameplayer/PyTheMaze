from action import Action
from joueur import Joueur


class Ouest(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        Ouest.joueur.avancerOuest()
        Ouest.joueur.perdreEnergie()

    def description(self):
        return "Permet de se déplacer vers l'Ouest"

    def getType(self):
        return self.getCategories()[0]
