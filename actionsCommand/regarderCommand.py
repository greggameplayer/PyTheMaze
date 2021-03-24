from action import ActionManager
from actions.regarder import Regarder


class RegarderCommand(ActionManager):

    def execute(self):
        """
        Execute the command.

        Args:
            self: (todo): write your description
        """
        return Regarder().execute()

    def description(self):
        """
        Return the description of the description.

        Args:
            self: (todo): write your description
        """
        return Regarder().description()

    def getType(self):
        """
        Returns the type of this node

        Args:
            self: (todo): write your description
        """
        return Regarder().getType()


ActionManager.getInstance().registerCommand("regarder", RegarderCommand())