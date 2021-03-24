from action import Action, ActionManager


class Help(Action):
    manager = ActionManager.getInstance()

    def execute(self):
        """
        Execute the command.

        Args:
            self: (todo): write your description
        """
        print("Actions possibles : ")
        Help.manager.descriptionCommande()
        input()

    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return "Permet au joueur d'avoir la description des commandes disponibles"

    def getType(self):
        """
        Returns the type of the type

        Args:
            self: (todo): write your description
        """
        return self.getCategories()[1]
