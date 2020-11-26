from objet import ObjetRamassable


class Clef(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self, joueur):
        self.joueur = joueur
        self._symboleWindowsTerminal = "🔑"
        self._symbole = "C"

    def description(self):
        return "Quelle jolie clé !, Il te manque " + str(10 - self.joueur.getCle()) + " pour pouvoir sortir !"

    def ramasser(self, joueur):
        joueur.mettreObjetDansLeSac(self)
        # Ajoute la clé au total du joueur
        joueur.gagnerCle()

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole
