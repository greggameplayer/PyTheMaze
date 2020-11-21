from action import Action
from joueur import Joueur


class Ramasser(Action):
    joueur = Joueur.getInstance("X", 100)

    def execute(self):
        case = Ramasser.joueur.getCaseCourante()
        if len(case.getObjets()) == 0:
            print("Mais... il n'y a rien à ramasser !")
        else:
            print("J'ai ramassé :")
            print(case.getObjets())
            for objet in case.getObjets():
                objet.ramasser(Ramasser.joueur)
                print(" - " + objet.description())
            case.getObjets().clear() # On est obliger de tout supprimer après avoir ramassé, car on ne peut pas modifier la liste sur laquelle on itere...
        input()
