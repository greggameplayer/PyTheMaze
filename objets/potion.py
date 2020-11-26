from objet import ObjetRamassable

class Potion(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self, energie):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
        self._energie = energie
        self._symbole = "."

    def utiliser(self, joueur):
        joueur.gagnerEnergie(self._energie)

    def description(self):
        return "Potion de "+str(self._energie)+" énergie(s)."

    def getSymbole(self):
        return self._symbole
