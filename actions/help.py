from action import Action, ActionManager


class Help(Action):
    manager = ActionManager.getInstance()

    def execute(self):
        print("Actions possbiles : ")
        Help.manager.descriptionCommande()
        input()

    def description(self):
        return "Permet au joueur d'avoir la description des commandes disponibles"