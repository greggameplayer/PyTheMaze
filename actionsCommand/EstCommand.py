from action import ActionManager
from actions.est import Est


class EstCommand(ActionManager):

    def execute(self):
        return Est().execute()

    def description(self):
        return Est().description()

    def getType(self):
        return Est().getType()


ActionManager.getInstance().registerCommand("d", EstCommand())
