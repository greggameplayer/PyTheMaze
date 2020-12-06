from objet import ObjetRamassable
from joueur import Joueur


class Crane(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """
    joueur = Joueur.getInstance("👤", "X", 100)

    __instance = None

    @staticmethod
    def getInstance():
        if Crane.__instance is None:
            Crane.__instance = Crane()
        return Crane.__instance

    def __init__(self):
        self._symboleWindowsTerminal = "💀"
        self._symbole = "U"

    def description(self):
        return "Donne ce crâne de cristal à Indiana Jones pour récupérer la carte du labyrinthe !"

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole

    def utiliser(self):
        pass