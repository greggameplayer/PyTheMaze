from action import Action
from joueur import Joueur


class Est(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        """
        Execute the command.

        Args:
            self: (todo): write your description
        """
        Est.joueur.avancerEst()
        Est.joueur.perdreEnergie()

    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return "Permet de se déplacer vers l'Est"

    def getType(self):
        """
        Return the type of the type

        Args:
            self: (todo): write your description
        """
        return self.getCategories()[0]