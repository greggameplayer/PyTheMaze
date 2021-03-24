from objet import ObjetRamassable
from joueur import Joueur


class Crane(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """
    joueur = Joueur.getInstance("👤", "X", 100)

    __instance = None

    @staticmethod
    def getInstance():
        """
        Return the instance of the current instance.

        Args:
        """
        if Crane.__instance is None:
            Crane.__instance = Crane()
        return Crane.__instance

    def __init__(self):
        """
        Initialize the symbol.

        Args:
            self: (todo): write your description
        """
        self._symboleWindowsTerminal = "💀"
        self._symbole = "U"

    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return "Donne ce crâne de cristal à Indiana Jones pour récupérer la carte du labyrinthe !"

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

    def utiliser(self):
        """
        Utiliser foriser.

        Args:
            self: (todo): write your description
        """
        pass