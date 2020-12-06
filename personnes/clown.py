from personnage import Personnage

class Clown(Personnage):
    """ Cette classe représente un clown qui salue le joueur lorsqu'il arrive sur la même case, il propose au joueur de détendre l'atmosphère 
    avec une blague. Le clown a une blague qu'on lui passe à la création dans le constructeur. """

    def __init__(self, blague):
    
        self._symbole = "W"
        self._symboleWindowsTerminal = "🤡"
        self._blague = blague

    def description(self):
        """ Renvoie la description du clown."""
        return "Un clown "

    def rencontrer(self):
        """ Affiche un message de salutation au joueur. """
    
        print("-Le clown: Bonjour à toi jeune entrepreneur ")

    def parler(self, joueur):
        """ Le clown propose de détendre l'atmsophère avec une blague. """
        print("-Clown: Aimerais-tu que je te raconte une petite blague ?(oui pour accepter)")
        entree = input("#>")
        if entree.lower() == "oui":
            print("-Le clown:"+self._blague)
        else:
            pass

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole
