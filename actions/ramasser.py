from action import Action
from joueur import Joueur


class Ramasser(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        """
        Executes the case.

        Args:
            self: (todo): write your description
        """
        case = Ramasser.joueur.getCaseCourante()
        if len(case.getObjets()) == 0:
            print("Mais... il n'y a rien à ramasser !")
        else:
            Ramasser.joueur.perdreEnergie()
            showRamasser = {}
            for obj in case.getObjets():
                obj.ramasser()
                test = True
                for clef, valeur in showRamasser.items():
                    if obj.__class__.__name__ + '(' + obj.description() + ')' == clef:
                        valeur.append(obj)
                        test = False
                if (test):
                    showRamasser[obj.__class__.__name__ + '(' + obj.description() + ')'] = [obj]

            index = 1
            print("J'ai ramassé : ")
            for clef, valeur in showRamasser.items():
                print('    - ' + clef + " : " + str(len(valeur)))
                index += 1

            case.getObjets().clear()  # On est obliger de tout supprimer après avoir ramassé, car on ne peut pas modifier la liste sur laquelle on itere...
        input()

    def description(self):
        """
        Return the description of this command.

        Args:
            self: (todo): write your description
        """
        return "Permet de ramasser un objet"

    def getType(self):
        """
        Returns the type of the type

        Args:
            self: (todo): write your description
        """
        return self.getCategories()[1]

