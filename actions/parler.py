from action import Action
from joueur import Joueur


class Parler(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        personnages = Parler.joueur.getCaseCourante().getPersonnages()
        if len(personnages) == 0:
            print("Allo ? allo allo allo allo allo répète l'écho")
        else:
            for personnage in personnages:
                personnage.parler(Parler.joueur)
        input()
    
    def description(self):
        return "Permet de parler à un pnj"
