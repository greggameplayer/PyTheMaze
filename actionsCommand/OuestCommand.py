from action import ActionManager
from actions.ouest import Ouest


class OuestCommand(ActionManager):

    def execute(self):
        return Ouest().execute()

    def description(self):
        return Ouest().description()
ActionManager.getInstance().registerCommand("q", OuestCommand())