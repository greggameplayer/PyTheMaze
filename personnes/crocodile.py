from joueur import Joueur
from personnage import Personnage
import random


class Crocodile(Personnage):
    """ Cette classe représente un crocodile, il croque lorsqu'on arrive dans sa case, ensuite il s'enfuit """

    def __init__(self):
        """ Constructeur. Paramètres :
         
        """
        self._joueur = Joueur.getInstance("", "", 100)
        self._symbole = "K"
        self._symboleWindowsTerminal = "🐊"

    def description(self):
        """ Renvoie la description du crocodile."""
        return "Croco"

    def rencontrer(self):
        """ Le crocodile fait perdre au joueur de l'energie en le mordant 
        quand celui ci tombe sur sa case """
        """ faire un if else pour le game over"""
        damage = random.randint(3, 15)
        for i in range(damage):
            self._joueur.perdreEnergie()
            self._joueur.energieChecker()
        if damage < 6:
            print("Tu viens de te faire mordre par un crocodile,\n heureusement pour toi il était végétarien! ")
        else:
            print("ptn il était grave vener la OOOUUFFF...")
        print("*Tu viens de perdre " + str(damage) + " d'énergies lors de ton fight avec le croco...*")
        self._joueur.getCaseCourante().supprimerPersonnage(self)
        input()

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
