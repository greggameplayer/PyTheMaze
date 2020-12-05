from personnage import Personnage
from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur

class Sphinx(Personnage):
    """ Cette classe représente la sortie du jeu """

    joueur = Joueur.getInstance("👤", "X", 100)
    labyrinthe = Labyrinthe.getInstance()

    def __init__(self):
        " Constructeur. Paramètres :"
        self._symboleWindowsTerminal = "🦅"
        self._symbole = "S"


    def description(self):
        """ Renvoie la description du sphinx."""
        return "L'animal mythologique représentant votre liberté!!!"

    def rencontrer(self):
        if Sphinx.joueur.getCle() == 10:
            print("*le Sphinx vous pose une question pour verifier la légitimité de votre liberté...*")
            reponse =input("...")
            if reponse == "":
                "sortie du jeu"
            else:
                print("*Le Sphinx vous vole une clé et s'envole *")
                print("Sphinx-> Retourner à vos ocupations, retrouver la clé volée, et revenez vers moi...")
                Sphinx.joueur.perdreCle()
                Sphinx.labyrinthe.deposerPersonneAleatoirement(self)
                Sphinx.joueur.carte = False
        else:
            print("Il vous manque encore " + 10 - int(Sphinx.joueur.getCle()) + "!!!")
            print("Continuer à les chercher")
        input()

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole