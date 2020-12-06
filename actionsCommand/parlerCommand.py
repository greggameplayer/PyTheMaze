from action import ActionManager
from actions.parler import Parler


class parlerCommand(ActionManager):

    def execute(self):
        return Parler().execute()

    def description(self):
        return Parler().description()

    def getType(self):
        return Parler().getType()


ActionManager.getInstance().registerCommand("parler", parlerCommand())
