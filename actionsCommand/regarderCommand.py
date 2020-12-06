from action import ActionManager
from actions.regarder import Regarder


class RegarderCommand(ActionManager):

    def execute(self):
        return Regarder().execute()

    def description(self):
        return Regarder().description()

    def getType(self):
        return Regarder().getType()


ActionManager.getInstance().registerCommand("regarder", RegarderCommand())