from action import ActionManager
from actions.est import Est


class EstCommand(ActionManager):

    def execute(self):
        """
        Execute the query.

        Args:
            self: (todo): write your description
        """
        return Est().execute()

    def description(self):
        """
        Return the description of this node.

        Args:
            self: (todo): write your description
        """
        return Est().description()

    def getType(self):
        """
        Returns the type of this item

        Args:
            self: (todo): write your description
        """
        return Est().getType()


ActionManager.getInstance().registerCommand("d", EstCommand())
