from action import Action
from joueur import Joueur


class Parler(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        """
        Execute the search.

        Args:
            self: (todo): write your description
        """
        personnages = Parler.joueur.getCaseCourante().getPersonnages()
        if len(personnages) == 0:
            print("Allo ? allo allo allo allo allo répète l'écho")
        else:
            for personnage in personnages:
                personnage.parler(Parler.joueur)
        input()
    
    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return "Permet de parler à un pnj"

    def getType(self):
        """
        Returns the type of the type

        Args:
            self: (todo): write your description
        """
        return self.getCategories()[1]

