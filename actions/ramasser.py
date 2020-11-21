from action import Action, ActionManager
from  joueur import Joueur


class Ramasser(Action):
    joueur = Joueur.getInstance("X", 100)

    def _init_(self):
        self.case = Ramasser.joueur.getCaseCourante()
        self.execute()
    
    def execute(self):
        if len(self.case.getObjets()) == 0:
            print("Mais... il n'y a rien à ramasser !")
        else:
            print("J'ai ramassé :")
            for objet in self.case.getObjets():
                objet.ramasser(Ramasser.joueur)
                print(" - " + objet.description())
            self.case.getObjets().clear()# On est obliger de tout supprimer après avoir ramassé, car on ne peut pas modifier la liste sur laquelle on itere...

    def info(self):
        pass
    def help(self):
        pass