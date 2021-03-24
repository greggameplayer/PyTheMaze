from action import ActionManager
from actions.help import Help


class HelpCommand(ActionManager):

    def execute(self):
        """
        Execute the command.

        Args:
            self: (todo): write your description
        """
        return Help().execute()

    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return Help().description()

    def getType(self):
        """
        Returns the type of this node

        Args:
            self: (todo): write your description
        """
        return Help().getType()


ActionManager.getInstance().registerCommand("help", HelpCommand())
