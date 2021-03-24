from action import ActionManager
from actions.sac import Sac


class SacCommand(ActionManager):

    def execute(self):
        """
        Execute the query.

        Args:
            self: (todo): write your description
        """
        return Sac().execute()

    def description(self):
        """
        Return the description of the description.

        Args:
            self: (todo): write your description
        """
        return Sac().description()

    def getType(self):
        """
        Returns the type of this object

        Args:
            self: (todo): write your description
        """
        return Sac().getType()


ActionManager.getInstance().registerCommand("sac", SacCommand())
