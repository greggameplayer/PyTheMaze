from action import ActionManager
from actions.sac import Sac


class SacCommand(ActionManager):

    def execute(self):
        return Sac().execute()


ActionManager.getInstance().registerCommand("sac", SacCommand())