from action import ActionManager
from actions.nord import Nord


class NordCommand(ActionManager):

    def execute(self):
        return Nord().execute()
    
    def description(self):
        return Nord().description()



ActionManager.getInstance().registerCommand("n", NordCommand())
