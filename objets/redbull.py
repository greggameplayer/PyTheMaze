from objet import ObjetRamassable
from joueur import Joueur

class Redbull(ObjetRamassable):
    joueur = Joueur.getInstance("👤", "X", 100)
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
        self._symboleWindowsTerminal = "🥫"
        self._symbole = "R"

    def utiliser(self):
        """
        Disconnects the joueur

        Args:
            self: (todo): write your description
        """
        Redbull.joueur.boireRedbull()
        print("JE VOLE !")
        return True

    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return "REDBULL donne des aileeees"

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

