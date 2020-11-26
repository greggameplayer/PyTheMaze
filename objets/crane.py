from objet import ObjetRamassable

class Crane(ObjetRamassable):
    """ Représente un crane qui une fois en la possession de indiana john permet de révélé toute la carte. """

    def __init__(self, energie, joueur):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
       def __init__(self,joueur):
        self.joueur = joueur

    def description(self):
        return "Quelle jolie clé !, Il te manque "+ str(10-self.joueur.nbCle) +" pour pouvoir sortir !"

    def ramasser(self,joueur):
        joueur.mettreObjetDansLeSac(self)
        # Ajoute la clé au total du joueur
        joueur.gagnerCle()