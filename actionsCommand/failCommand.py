from action import ActionManager
from actions.fail import Fail


class FailCommand(ActionManager):

    def execute(self):
        return Fail().execute()


ActionManager.getInstance().registerCommand("fail", FailCommand())