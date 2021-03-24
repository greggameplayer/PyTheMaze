from action import ActionManager
from actions.ramasser import Ramasser


class RamasserCommand(ActionManager):

    def execute(self):
        """
        Execute the query and return the result.

        Args:
            self: (todo): write your description
        """
        return Ramasser().execute()

    def description(self):
        """
        Return the description of this description.

        Args:
            self: (todo): write your description
        """
        return Ramasser().description()

    def getType(self):
        """
        : return : the type

        Args:
            self: (todo): write your description
        """
        return Ramasser().getType()


ActionManager.getInstance().registerCommand("ramasser", RamasserCommand())