from action import Action
from joueur import Joueur


class Nord(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        Nord.joueur.avancerNord()
        Nord.joueur.perdreEnergie()

    def description(self):
        return "Permet d'aller au nord"

    def getType(self):
        return self.getCategories()[0]
