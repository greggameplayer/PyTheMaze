from action import ActionManager
from actions.regarder import Regarder


class RegarderCommand(ActionManager):

    def execute(self):
        return Regarder().execute()


ActionManager.getInstance().registerCommand("regarder", RegarderCommand())