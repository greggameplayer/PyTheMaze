from action import ActionManager
from actions.est import Est
import keyboard


class EstCommand(ActionManager):

    def execute(self):
        return Est().execute()

    def description(self):
        return Est().description()

ActionManager.getInstance().registerCommand("d", EstCommand())
