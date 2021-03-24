from action import ActionManager
from actions.parler import Parler


class parlerCommand(ActionManager):

    def execute(self):
        """
        Execute the query.

        Args:
            self: (todo): write your description
        """
        return Parler().execute()

    def description(self):
        """
        The description of the description.

        Args:
            self: (todo): write your description
        """
        return Parler().description()

    def getType(self):
        """
        Returns the type of this object

        Args:
            self: (todo): write your description
        """
        return Parler().getType()


ActionManager.getInstance().registerCommand("parler", parlerCommand())
