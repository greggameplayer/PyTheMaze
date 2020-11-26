from personnage import Personnage
import random

class Indiana(Personnage):
    """ Cette classe représente un Personnage qui permet quand un utilisateur lui donne le crane il l'echange contre la carte. """

    def __init__(self, couleur):
      

    def description(self):
        """ Renvoie la description de Indiana."""
        return "Un Indiana " 

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        TODO: on pourrait avoir un message de salutation plus varié en le tirant aléatoirement ici, ou dans le constructeur pour qu'un même perroquet salue toujours de la même façon.
        """
        print("Un Indiana vous salue !")
        input()

    def parler(self, joueur):
        """ Le Indiana pose des questions. """
        print("Indiana : Avez vous la carte ? (Oui/Non)")
        entree = input("#>")
            if entree == "Oui":
                #on lance la fonction de découverte et suprresion du crane
            else:
                print("Passe-ton chemin, est cherche  la carte")
      