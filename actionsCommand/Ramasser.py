from action import ActionManager
from actions.ramasser import Ramasser


class RamasserCommand(ActionManager):

    def execute(self):
        return Ramasser().execute()


ActionManager.getInstance().registerCommand("ramasser", RamasserCommand())