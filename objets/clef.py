from objet import ObjetRamassable
from joueur import Joueur


class Clef(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    joueur = Joueur.getInstance("👤", "X", 100)

    def __init__(self):
        self._symboleWindowsTerminal = "🔑"
        self._symbole = "C"

    def description(self):
        return "Il te manque " + str(10 - self.joueur.getCle()) + " pour pouvoir sortir !"

    def ramasser(self):
        if Clef.joueur.getCle() < 10:
            Clef.joueur.mettreObjetDansLeSac(self)
            Clef.joueur.gagnerCle()
        else:
            print("Vous avez déjà les 10 clefs requises... dirigez-vous vers le sphinx !")
            input()

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole

    def utiliser(self):
        if Clef.joueur.getCle() == 10:
            print("Va voir le sphinx jeune Padawan")
        else:
            print("Il est trop tôt pour utiliser la clé jeune Padawan!")
        return False
