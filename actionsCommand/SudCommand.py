from action import ActionManager
from actions.sud import Sud


class SudCommand(ActionManager):

    def execute(self):
        """
        Executes the sql query.

        Args:
            self: (todo): write your description
        """
        return Sud().execute()

    def description(self):
        """
        Return the description of the description.

        Args:
            self: (todo): write your description
        """
        return Sud().description()

    def getType(self):
        """
        Returns the type of this object

        Args:
            self: (todo): write your description
        """
        return Sud().getType()


ActionManager.getInstance().registerCommand("s", SudCommand())
