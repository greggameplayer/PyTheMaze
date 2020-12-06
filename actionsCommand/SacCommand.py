from action import ActionManager
from actions.sac import Sac


class SacCommand(ActionManager):

    def execute(self):
        return Sac().execute()

    def description(self):
        return Sac().description()

    def getType(self):
        return Sac().getType()


ActionManager.getInstance().registerCommand("sac", SacCommand())
