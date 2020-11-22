from action import ActionManager
from actions.parler import Parler


class parlerCommand(ActionManager):

    def execute(self):
        return Parler().execute()
    def description(self):
        return Parler().description()

ActionManager.getInstance().registerCommand("parler", parlerCommand())
