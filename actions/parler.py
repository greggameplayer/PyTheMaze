from action import Action, ActionManager
from  joueur import Joueur

class Parler(Action):
    joueur = Joueur.getInstance()

    def _init_(self):
        self.personnages = Parler.joueur.getCaseCourante().getPersonnages()
        self.execute()

    def execute(self):
        if len(self.personnages) == 0:
            print("Allo ? allo allo allo allo allo répète l'écho")
        else:
            for personnage in self.personnages:
                personnage.parler(Parler.joueur)    
    
    def info(self):
        pass
    def help(self):
        pass