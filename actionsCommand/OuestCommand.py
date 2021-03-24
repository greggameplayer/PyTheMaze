from action import ActionManager
from actions.ouest import Ouest


class OuestCommand(ActionManager):

    def execute(self):
        """
        Returns the result of the query.

        Args:
            self: (todo): write your description
        """
        return Ouest().execute()

    def description(self):
        """
        The description of the description.

        Args:
            self: (todo): write your description
        """
        return Ouest().description()

    def getType(self):
        """
        Returns the type of this node

        Args:
            self: (todo): write your description
        """
        return Ouest().getType()


ActionManager.getInstance().registerCommand("q", OuestCommand())