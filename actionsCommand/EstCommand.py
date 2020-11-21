from action import ActionManager
from actions.est import Est


class EstCommand(ActionManager):

    def execute(self):
        return Est().execute()


ActionManager.getInstance().registerCommand("e", EstCommand())
