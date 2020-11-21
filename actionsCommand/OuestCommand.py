from action import ActionManager
from actions.ouest import Ouest


class OuestCommand(ActionManager):

    def execute(self):
        return Ouest().execute()


ActionManager.getInstance().registerCommand("o", OuestCommand())