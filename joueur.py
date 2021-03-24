from labyrinthe.labyrinthe import Case
from labyrinthe.labyrinthe import Labyrinthe
from objetFactory import ObjetFactoryPrincipale


class Joueur:
    __instance = None

    @staticmethod
    def getInstance(symboleWindowsTerminal, symbole, atb2):
        """
        Returns a jouoleeur.

        Args:
            symboleWindowsTerminal: (int): write your description
            symbole: (int): write your description
            atb2: (str): write your description
        """
        if Joueur.__instance is None:
            Joueur.__instance = Joueur(symboleWindowsTerminal, symbole, atb2)
        return Joueur.__instance

    def __init__(self, symboleWindowsTerminal, symbole, energieInitiale):
        """
        Initializes the energies.

        Args:
            self: (todo): write your description
            symboleWindowsTerminal: (todo): write your description
            symbole: (str): write your description
            energieInitiale: (todo): write your description
        """
        # La case sur laquelle se situe le joueur
        self.__caseCourante = Case()
        self.__symbole = symbole
        self.__symboleWindowsTerminal = symboleWindowsTerminal
        self.__energieMax = 80  # TODO: mettre le niveau d'énergie max en fonction du paramétrage du jeu
        self.__energie = energieInitiale
        self._sac = []  # On commence avec un sac vide
        self.setEnergie(energieInitiale)
        self.nbCle = 0
        self.voler = False

    def getEnergie(self):
        """ Renvoie le niveau d'énergie du joueur. """
        return self.__energie

    def setEnergie(self, valeur):
        """ Fixe l'energie du joueur à une valeur donnée, sans pouvoir dépasser le maximum autorisé. """
        self.__energie = min(valeur, self.__energieMax)

    def perdreEnergie(self):
        """ Retire un point d'énergie au joueur. """
        self.__energie -= 1

    def gagnerEnergie(self, combien):
        """ Ajoute de l'énergie au joueur. Paramètres :
        - combien : le montant d'énergie ajouté
        """
        self.__energie = min(self.__energie + combien, self.__energieMax)

    def getCaseCourante(self):
        """
        : returns : class

        Args:
            self: (todo): write your description
        """
        return self.__caseCourante

    def setCaseCourante(self, case):
        """
        Sets the case for the case.

        Args:
            self: (todo): write your description
            case: (todo): write your description
        """
        # Enlève le joueur de la case sur laquelle il se trouve actuellement
        self.__caseCourante.supprimerJoueur()
        # Ajoute le joueur sur la nouvelle case
        self.__caseCourante = case
        case.ajouterJoueur(self)
        # Découvre les cases alentour
        self.decouvreAlentour()
        # Rencontre tous les personnages potentiellements présents sur la case
        for personnage in case.getPersonnages():
            personnage.rencontrer()

    def decouvreAlentour(self):
        """
        Removes the case.

        Args:
            self: (todo): write your description
        """
        self.__caseCourante.decouvrir()
        if self.__caseCourante.estOuvertNord(): self.__caseCourante.getCaseNord().decouvrir()
        if self.__caseCourante.estOuvertSud(): self.__caseCourante.getCaseSud().decouvrir()
        if self.__caseCourante.estOuvertEst(): self.__caseCourante.getCaseEst().decouvrir()
        if self.__caseCourante.estOuvertOuest(): self.__caseCourante.getCaseOuest().decouvrir()

    def reinitionalisationDecouverte(self):
        """
        Recompute all case case.

        Args:
            self: (todo): write your description
        """
        for case in Labyrinthe.getInstance().cases:
            case.cacher()
        self.__caseCourante.decouvrir()

    def toutDecouvrir(self):
        """
        Decouvrir case.

        Args:
            self: (todo): write your description
        """
        for case in Labyrinthe.getInstance().cases:
            case.decouvrir()
        self.__caseCourante.decouvrir()

    def getSymbole(self, isWindowsTerminal):
        """
        Returns the positive scalar : class.

        Args:
            self: (todo): write your description
            isWindowsTerminal: (bool): write your description
        """
        if isWindowsTerminal:
            return self.__symboleWindowsTerminal
        else:
            return self.__symbole

    def avancerNord(self):
        """
        Sets the untancer.

        Args:
            self: (todo): write your description
        """
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertNord():
            self.setCaseCourante(caseCourante.getCaseNord())
        elif self.getVoler():
            self.setCaseCourante(caseCourante.getCaseNord())
            self.plusDeRedbull()
        else:
            raise ValueError("Pas de passage par là...")

    def avancerSud(self):
        """
        Sets the uuid.

        Args:
            self: (todo): write your description
        """
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertSud():
            self.setCaseCourante(caseCourante.getCaseSud())
        elif self.getVoler():
            self.setCaseCourante(caseCourante.getCaseSud())
            self.plusDeRedbull()
        else:
            raise ValueError("Pas de passage par là...")

    def avancerEst(self):
        """
        Sets the case.

        Args:
            self: (todo): write your description
        """
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertEst():
            self.setCaseCourante(caseCourante.getCaseEst())
        elif self.getVoler():
            self.setCaseCourante(caseCourante.getCaseEst())
            self.plusDeRedbull()
        else:
            raise ValueError("Pas de passage par là...")

    def avancerOuest(self):
        """
        Sets the test case.

        Args:
            self: (todo): write your description
        """
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertOuest():
            self.setCaseCourante(caseCourante.getCaseOuest())
        elif self.getVoler():
            self.setCaseCourante(caseCourante.getCaseOuest())
            self.plusDeRedbull()
        else:
            raise ValueError("Pas de passage par là...")

    def printEnergie(self, isWindowsTerminal):
        """ Petite fonction utilitaire pour afficher la jauge d'énergie sur la console. """
        if isWindowsTerminal:
            print(" ENERGIE " + "◼" * self.__energie + (" " * (self.__energieMax - self.__energie)) + "|")
        else:
            print(" ENERGIE " + ">" * self.__energie + " " * (self.__energieMax - self.__energie) + "|")

    def getSac(self):
        """
        : return : attribute.

        Args:
            self: (todo): write your description
        """
        return self._sac

    def mettreObjetDansLeSac(self, objet):
        """ Met l'objet passé en paramètre dans le sac du joueur."""
        self._sac.append(objet)

    def gagnerCle(self):
        """
        Set the gagCle

        Args:
            self: (todo): write your description
        """
        self.nbCle += 1

    def perdreCle(self):
        """
        Perform dedreCle

        Args:
            self: (todo): write your description
        """
        self.nbCle -= 1
        for obj in self.getSac():
            if obj.__class__.__name__ == "Clef":
                self.getSac().remove(obj)
                break
        Labyrinthe.getInstance().deposerObjetAleatoirement(ObjetFactoryPrincipale.getInstance().creerObjet("clef"), self.getInstance("", "", 100))

    def getCle(self):
        """
        Get the next numpy.

        Args:
            self: (todo): write your description
        """
        return self.nbCle

    def boireRedbull(self):
        """
        Prints the current volume

        Args:
            self: (todo): write your description
        """
        print("OUIIIIII")
        self.voler = True

    def plusDeRedbull(self):
        """
        Disconnects the volume

        Args:
            self: (todo): write your description
        """
        print("NONNNN")
        self.voler = False

    def getVoler(self):
        """
        Returns the voler

        Args:
            self: (todo): write your description
        """
        return self.voler

    def energieChecker(self):
        """
        Returns true if the checker is in a listener.

        Args:
            self: (todo): write your description
        """
        if self.__energie == 0:
            print("""
            .-----..---.-..--------..-----. .-----..--.--..-----..----.
            |  _  ||  _  ||        ||  -__| |  _  ||  |  ||  -__||   _|
            |___  ||___._||__|__|__||_____| |_____| \___/ |_____||__|
            |_____|
            """)
            return True

