from action import Action
from joueur import Joueur


class Sac(Action):
    joueur = Joueur.getInstance("👤", "X", 100)

    def execute(self):
        sac = Sac.joueur.getSac()
        if(len(sac)) == 0:
            print("Le sac est vide")
            input()
        else:
            print("Le sac contient: ")
            
            showSac= {}
            for obj in sac:
                test = True
                for clef, valeur in showSac.items():
                    if obj.__class__.__name__+ '('+ obj.description() +')' == clef:
                        valeur.append(obj)
                        test = False
                if(test):
                    showSac[obj.__class__.__name__ + '('+ obj.description() +')'] = [obj]
            
            index = 1
            for clef, valeur in showSac.items():
                print(str(index) + '- ' + clef + " : " + str(len(valeur)))
                index+=1

            while True:
                choice = input("Pour utiliser un objet, taper son numéro, ou appyer sur entrée pour ne rien faire. ")
                if choice == "":
                    break
                else :
                    try : 
                        num = int(choice)
                        choix = list(showSac.values())[num-1]
                        obj = choix[0]
                        test = obj.utiliser()
                        if(test):
                            sac.remove(obj)
                        input()
                        break
                    except Exception:
                        print("\nWhere is the item ? \nIt is not in the list !\n")

    def description(self):
        return "Permet de se regarfer l'inventaire de son sac"