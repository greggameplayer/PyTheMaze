from action import ActionManager
from actions.nord import Nord


class NordCommand(ActionManager):

    def execute(self):
        """
        Executes the nord query.

        Args:
            self: (todo): write your description
        """
        return Nord().execute()
    
    def description(self):
        """
        Return the description of this element.

        Args:
            self: (todo): write your description
        """
        return Nord().description()

    def getType(self):
        """
        Returns the type of this object

        Args:
            self: (todo): write your description
        """
        return Nord().getType()


ActionManager.getInstance().registerCommand("z", NordCommand())
