from action import ActionManager
from actions.sud import Sud


class SudCommand(ActionManager):

    def execute(self):
        return Sud().execute()
    def description(self):
        return Sud().description()

ActionManager.getInstance().registerCommand("s", SudCommand())
