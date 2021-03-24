from personnage import Personnage
import random
from joueur import Joueur

class Singe(Personnage):
    """ Cette classe représente un singe qui vole une clé lorsqu'on arrive dans sa case, ensuite il s'enfuit """

    joueur = Joueur.getInstance("👤", "X", 100)

    def __init__(self):
        """ Constructeur. Paramètres :
        - couleur : la couleur du perroquet (chaine de caractères)
        """
        self._symboleWindowsTerminal = "🐵"
        self._symbole = "S"


    def description(self):
        """ Renvoie la description du perroquet."""
        return "Un singe"

    def rencontrer(self):
        """
        Rencontrer input

        Args:
            self: (todo): write your description
        """
        #Vole une clé au joueur
        if Singe.joueur.getCle() !=0:
            print("Oh nonnn, le singe vient de te piquer une clef !")
            Singe.joueur.perdreCle()
            print("Vous avez maintenant "+ str(Singe.joueur.nbCle) + " clef")
            Singe.joueur.getCaseCourante().supprimerPersonnage(self)
        else:
            print("Le singe vous dévisage..")
        input()

    def parler(self, joueur):
        """
        Æł¥è¯¢æīĳľçº¿

        Args:
            self: (todo): write your description
            joueur: (int): write your description
        """
        print("wouuuuuaaaaaInInIn WWWoouaaaahhInInInIn !!!")

    def getSymbole(self, isWindowsTerminal):
        """
        Returns the integral of a given character.

        Args:
            self: (todo): write your description
            isWindowsTerminal: (bool): write your description
        """
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole
