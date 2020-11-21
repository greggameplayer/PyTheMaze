from action import Action, ActionManager
from  joueur import Joueur

class Sac(Action):
    joueur = Joueur.getInstance("X", 100)

    def _init_(self):
        self.sac = Sac.joueur.getSac()
        self.execute()

    def execute(self):
        if(len(self.sac)) == 0:
            print("Le sac est vide")
            input()
        else:
            print("Le sac contient: ")
            index = 0
            for obj in self.sac:
                print(str(index+1)+" - "+obj.description())
                index += 1
            choice = input("Pour utiliser un objet, taper son numéro, ou entrée pour ne rien faire. ")
            try:
                num = int(choice)
                obj = self.sac[num-1]
                self.sac.remove(obj)
                obj.utiliser(Sac.joueur)
            except:
                pass # En cas d'erreur, c'est que l'entrée est invalide, on ne fait rien
    
    
    def info(self):
        pass
    def help(self):
        pass