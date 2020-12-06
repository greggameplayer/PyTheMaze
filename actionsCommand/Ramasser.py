from action import ActionManager
from actions.ramasser import Ramasser


class RamasserCommand(ActionManager):

    def execute(self):
        return Ramasser().execute()

    def description(self):
        return Ramasser().description()

    def getType(self):
        return Ramasser().getType()


ActionManager.getInstance().registerCommand("ramasser", RamasserCommand())