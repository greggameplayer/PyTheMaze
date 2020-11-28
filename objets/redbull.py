from objet import ObjetRamassable
from joueur import Joueur

class Redbull(ObjetRamassable):
    joueur = Joueur.getInstance("👤", "X", 100)
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self, energie):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
        self._energie = energie
        self._symboleWindowsTerminal = "🥫"
        self._symbole = "R"

    def utiliser(self):
        Redbull.joueur.gagnerEnergie(self._energie)
        Redbull.joueur.boireRedbull()
        print("JE VOLE !")
        return True

    def description(self):
        return "REDBULL donne des aileeees"

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole

