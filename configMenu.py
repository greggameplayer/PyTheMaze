import os


class ConfigMenu:
    __instance = None

    @staticmethod
    def getInstance(symboleWindowsTerminal, symbole, atb2):
        """
        Returns the configuration object for the given configuration.

        Args:
            symboleWindowsTerminal: (int): write your description
            symbole: (int): write your description
            atb2: (str): write your description
        """
        if ConfigMenu.__instance is None:
            ConfigMenu.__instance = ConfigMenu()
        return ConfigMenu.__instance

    def __init__(self):
        """
        Initialize this object.

        Args:
            self: (todo): write your description
        """
        self._choice = ""

    def ask(self):
        """
        Prompt user input

        Args:
            self: (todo): write your description
        """
        while True:
            print("Veuillez choisir un niveau de difficulté :")
            print("1) Facile")
            print("2) Moyen")
            print("3) Difficile")
            self._choice = input("#> ")
            if self._choice in ["1", "2", "3"]:
                os.system('cls' if os.name == 'nt' else 'clear')
                return self._choice
