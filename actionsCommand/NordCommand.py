from action import ActionManager
from actions.nord import Nord


class NordCommand(ActionManager):

    def execute(self):
        return Nord().execute()
    
    def description(self):
        return Nord().description()

    def getType(self):
        return Nord().getType()


ActionManager.getInstance().registerCommand("z", NordCommand())
