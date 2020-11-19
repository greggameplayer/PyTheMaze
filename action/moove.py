from action import Action, ActionManager
from  joueur import Joueur

class Moove(Action):
    
    joueur = Joueur() #Demander aux autres comment appelr joueur 

    def __init__(self, letter):
        self.action = letter

    def execute(self):
        if self.action == "n":
            try:
                joueur.avancerNord()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif self.action == "s":
            try:
                joueur.avancerSud()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif self.action == "e":
            try:
                joueur.avancerEst()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif self.action == "o":
            try:
                joueur.avancerOuest()
            except:
                print("Ouch, ce mur fait mal...")
                input()
