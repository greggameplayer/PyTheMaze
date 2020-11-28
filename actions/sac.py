from action import Action
from joueur import Joueur


class Sac(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        sac = Sac.joueur.getSac()
        if(len(sac)) == 0:
            print("Le sac est vide")
            input()
        else:
            print("Le sac contient: ")
            index = 0
            for obj in sac:
                print(str(index+1)+" - "+obj.description())
                index += 1
            choice = input("Pour utiliser un objet, taper son numéro, ou entrée pour ne rien faire. ")
            num = int(choice)
            obj = sac[num-1]
            obj.utiliser(Sac.joueur)
            sac.remove(obj)

    def description(self):
        return "Permet de se regarfer l'inventaire de son sac"