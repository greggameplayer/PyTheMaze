from personnage import Personnage


class Indiana(Personnage):
    """ Cette classe représente un Personnage qui permet quand un utilisateur lui donne le crane il l'echange contre la carte. """

    __instance = None

    @staticmethod
    def getInstance():
        if Indiana.__instance is None:
            Indiana.__instance = Indiana()
        return Indiana.__instance

    def __init__(self):
        self._symbole = "I"
        self._symboleWindowsTerminal = "🤠"

    def description(self):
        """ Renvoie la description de Indiana."""
        return "Un Indiana"

    def rencontrer(self):
        print("Le célébre Indiana Jones vous salue !")
        print("Si vous avez le crâne de crystal il vous donnera la carte")

    def parler(self, joueur):
        """ Le Indiana pose des questions. """
        print("Indiana regarde si vous avez le crâne de cristal...")
        input()
        for objet in joueur.getSac():
            if objet.__class__.__name__ == "Crane":
                joueur.toutDecouvrir()
                print("*Indiana Jones vous donne la carte du labyrinthe.\nVous étiez à -10 de vision, tel une taupe, mtn vous voila à +10...\nAh non pardon, plutot à 0.00000!!!*")
            else:
                print("T'as cru c'est gratuit??? Kastoa, et cherche le crâne de cristal si tu veux que je te donne la carte...")
        input()

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole
