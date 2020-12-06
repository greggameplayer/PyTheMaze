import os


class ConfigMenu:
    __instance = None

    @staticmethod
    def getInstance(symboleWindowsTerminal, symbole, atb2):
        if ConfigMenu.__instance is None:
            ConfigMenu.__instance = ConfigMenu()
        return ConfigMenu.__instance

    def __init__(self):
        self._choice = ""

    def ask(self):
        while True:
            print("Veuillez choisir un niveau de difficulté :")
            print("1) Facile")
            print("2) Moyen")
            print("3) Difficile")
            self._choice = input("#> ")
            if self._choice in ["1", "2", "3"]:
                os.system('cls' if os.name == 'nt' else 'clear')
                return self._choice
