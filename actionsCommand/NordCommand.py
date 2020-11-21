from action import ActionManager
from actions.nord import Nord


class NordCommand(ActionManager):

    def execute(self):
        return Nord().execute()


ActionManager.getInstance().registerCommand("n", NordCommand())
