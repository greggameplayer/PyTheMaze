import os, random

from personnage import Personnage
from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur


class Sphinx(Personnage):
    """ Cette classe représente la sortie du jeu """
    joueur = Joueur.getInstance("👤", "X", 100)
    labyrinthe = Labyrinthe.getInstance()

    __instance = None

    @staticmethod
    def getInstance():
        if Sphinx.__instance is None:
            Sphinx.__instance = Sphinx()
        return Sphinx.__instance

    def __init__(self):
        " Constructeur. Paramètres :"
        self._symboleWindowsTerminal = "🦅"
        self._symbole = "T"
        self._questions = {
            "Quel est l'être doué de la voix qui a quatre pieds le matin, deux à midi et trois le soir ?": ["l'homme","nous","l'humain","humain","homme"],
            "Je ne peux pas marcher, j’ai pourtant un dos et quatre pieds. Qui suis-je ?": ["une chaise", "chaise"],
            """Un homme se réveille chez lui, dans le noir complet. Dans son tiroir, il y a 6 chaussettes noires, 4 blanches et deux rouges.\n 
            Combien doit-il prendre de chaussettes au minimum pour être certain d’avoir deux chaussettes de la même couleur ?""": [
                "quatre", "4"],
            "Qu’est-ce qui est jaune avec une cape ?": ["une banane", "banane"],
            "je suis noir, je deviens rouge, et je finis blanc.\nQui suis-je?": ["le charbon", "charbon"],
            "lisez cette chaine: g-k-c-1-9-i-r": ["j'ai cassé un neuf hier"]
        }

    def description(self):
        """ Renvoie la description du sphinx."""
        return "L'animal mythologique représentant votre liberté!!!"

    def parler(self, joueur):
        if Sphinx.joueur.getCle() >= 10:
            print("*le Sphinx vous pose une question pour verifier la légitimité de votre liberté...*")
            question = random.choice(list(self._questions.keys()))
            reponse = input(question).lower()
            for response in self._questions[question]:
                if reponse == response:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("""
                .____    ._____.                  __       __  
                |    |   |__\_ |__   ____________/  |_  __/_  
                |    |   |  || __ \_/ __ \_  __ \   __\/ __ \ 
                |    |___|  || \_\ \  ___/|  | \/|  | \  ___/ 
                |_______ \__||___  /\___  >__|   |__|  \___  >
                        \/       \/     \/                 \/ 
                """)
                    exit(0)
            print("*Le Sphinx vous vole une clé et s'envole *")
            print("Sphinx-> Retourner à vos occupations, retrouver la clé volée, et revenez vers moi...")
            Sphinx.joueur.perdreCle()
            Sphinx.labyrinthe.deposerPersonneAleatoirement(self.getInstance(), Sphinx.joueur)
            Sphinx.joueur.getCaseCourante().supprimerPersonnage(self.getInstance())
            Sphinx.joueur.reinitionalisationDecouverte()
        else:
            print("Il vous manque encore " + str(10 - int(Sphinx.joueur.getCle())) + "clef !!!")
            print("Continuer à les chercher...")
        input()

    def rencontrer(self):
        pass

    def getSymbole(self, isWindowsTerminal):
        if isWindowsTerminal:
            return self._symboleWindowsTerminal
        else:
            return self._symbole
