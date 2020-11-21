from action import ActionManager
from actions.sac import Sac


class SacCommand(ActionManager):

    def execute(self):
        return Sac().execute()
    def description(self):
        return Sac().description()

ActionManager.getInstance().registerCommand("sac", SacCommand())