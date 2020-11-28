from personnage import Personnage
import random

class Singe(Personnage):
    """ Cette classe représente un singe qui vole une clé lorsqu'on arrive dans sa case, ensuite il s'enfuit """

    def __init__(self):
        """ Constructeur. Paramètres :
        - couleur : la couleur du perroquet (chaine de caractères)
        """
        self._symboleWindowsTerminal = "🐵"
        self._symbole = "S"


    def description(self):
        """ Renvoie la description du perroquet."""
        return "Un singe"

    def rencontrer(self, joueur):
        #Vole une clé au joueur
        if joueur.getCle() !=0:
            print("Oh nonnn, le singe vient de te piquer une clef !")
            print(joueur.getSac())
            joueur.perdreCle()
            print("Vous avez maintenant "+ str(joueur.nbCle) + " clef")
        else:
            print("Le singe vous dévisage")

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole
