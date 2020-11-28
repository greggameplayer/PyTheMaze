from objet import ObjetRamassable
from joueur import Joueur

class Potion(ObjetRamassable):
    joueur = Joueur.getInstance("👤", "X", 100)

    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self, energie):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
        self._energie = energie
        self._symboleWindowsTerminal = "🧃"
        self._symbole = "."

    def utiliser(self):
        Potion.joueur.gagnerEnergie(self._energie)
        print("J'ai récupéré " + str(self._energie) + " point(s) d'énergie ! Je pète le feu !!")
        return True

    def description(self):
        return "Potion de "+str(self._energie)+" énergie(s)."

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole
