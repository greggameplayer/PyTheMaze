from action import ActionManager
from actions.help import Help


class HelpCommand(ActionManager):

    def execute(self):
        return Help().execute()

    def description(self):
        return Help().description()

ActionManager.getInstance().registerCommand("help", HelpCommand())
