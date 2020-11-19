from action import Action, ActionManager
from  joueur import Joueur

class Bouger(Action):
    
    joueur = Joueur.getInstance() 

    def __init__(self, letter):
        self.action = letter

    def execute(self):
        if self.action == "n":
            try:
                Bouger.joueur.avancerNord()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif self.action == "s":
            try:
                Bouger.joueur.avancerSud()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif self.action == "e":
            try:
                Bouger.joueur.avancerEst()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif self.action == "o":
            try:
                Bouger.joueur.avancerOuest()
            except:
                print("Ouch, ce mur fait mal...")

    def info(self):
        print("Permet à votre personne de se déplacer")

    def help(self):
        print("""
Permet à votre personne de se déplacer :
Nord = n, 
Sud = s,
Ouest = o,
Est = e """)