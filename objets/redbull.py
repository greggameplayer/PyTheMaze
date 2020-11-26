from objet import ObjetRamassable

class Redbull(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self, energie, joueur):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
        self._energie = energie
        self.joueur = joueur

    def utiliser(self,joueur):
        joueur.gagnerEnergie(self._energie)
        joueur.boireRedbull()
        print("JE VOLE !")

    def description(self):
        return "REDBULL donne des aileeees"



