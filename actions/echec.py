from action import Action


class Sac(Action):

    def _init_(self):
        pass

    def execute(self):
        print("Moi pas comprendre...")
        print("Mon vocabulaire est limité  à n, s, e, o, regarder, ramasser, sac et parler.")

    def getType(self):
        return self.getCategories()[1]
