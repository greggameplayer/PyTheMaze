from action import Action
from joueur import Joueur


class Sud(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        """
        Execute the command.

        Args:
            self: (todo): write your description
        """
        Sud.joueur.avancerSud()
        Sud.joueur.perdreEnergie()

    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return "Permet de se déplacer vers le sud"

    def getType(self):
        """
        Return the type of the type

        Args:
            self: (todo): write your description
        """
        return self.getCategories()[0]
