from action import Action


class Sac(Action):

    def _init_(self):
        """
        Initialize the state

        Args:
            self: (todo): write your description
        """
        pass

    def execute(self):
        """
        Execute the command.

        Args:
            self: (todo): write your description
        """
        print("Moi pas comprendre...")
        print("Mon vocabulaire est limité  à n, s, e, o, regarder, ramasser, sac et parler.")

    def getType(self):
        """
        Returns the type of the type

        Args:
            self: (todo): write your description
        """
        return self.getCategories()[1]
