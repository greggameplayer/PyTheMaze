from objet import ObjetRamassable


class Clef(ObjetRamassable) :

    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """
    def __init__(self,joueur):
        self.joueur = joueur

    def description(self):
        return "Quelle jolie clé !, Il te manque "+ str(10-self.joueur.nbCle) +" pour pouvoir sortir !"

    def ramasser(self,joueur):
        joueur.mettreObjetDansLeSac(self)
        # Ajoute la clé au total du joueur
        joueur.gagnerCle()