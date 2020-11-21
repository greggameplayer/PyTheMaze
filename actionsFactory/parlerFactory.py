from action import ActionManager
from actions.parler import Parler


class parlerFactory(ActionManager):

    def execute(self):
        return Parler().execute()


ActionManager.getInstance().registerCommand("parler", parlerFactory())
