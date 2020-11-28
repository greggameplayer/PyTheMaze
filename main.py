from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur

from objetFactory import ObjetFactoryPrincipale

from action import ActionManager
from personnesFactory import PersonnesFactoryPrincipale

import os, sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# now, to clear the screen
cls()

print("""

   .____                                                          
   |    |    ____                                                 
   |    |  _/ __ \                                                
   |    |__\  ___/                                                
   |_______ \___  >                                               
           \/   \/                                                
.____          ___.                 .__        __  .__            
|    |   _____ \_ |__ ___.__._______|__| _____/  |_|  |__   ____  
|    |   \__  \ | __ <   |  |\_  __ \  |/    \   __\  |  \_/ __ \ 
|    |___ / __ \| \_\ \___  | |  | \/  |   |  \  | |   Y  \  ___/ 
|_______ (____  /___  / ____| |__|  |__|___|  /__| |___|  /\___  >
        \/    \/    \/\/                    \/          \/     \/
        
         
""")

if (sys.platform == "win32" and os.environ.get("WT_SESSION")) is None:
    print("   WARNING: Merci d'utiliser Windows Terminal pour une meilleure expérience (support des emojis)")
    print("   Il est téléchargeable via le lien suivant : https://www.microsoft.com/fr-fr/p/windows-terminal/9n0dx20hk701\n")

input("   Appuyer sur 'Entrée' pour entrer dans le labyrinthe")

cls()

# Création des objets
# TODO: récupérer les attributs via un menu de configuration
joueur = Joueur.getInstance("👤", "X", 100)
l = Labyrinthe.getInstance()
l.deposerJoueurAleatoirement(joueur)
factoryObjet = ObjetFactoryPrincipale.getInstance()
factoryObjet.loadFactoryPlugins()
factoryPersonne = PersonnesFactoryPrincipale.getInstance()
factoryPersonne.loadFactoryPlugins()
actionManager = ActionManager.getInstance()
actionManager.loadActionPlugins()

# Generation de 70 potions aléatoirement
for i in range(70):
    l.deposerObjetAleatoirement(factoryObjet.creerObjet("potion"))
    l.deposerObjetAleatoirement(factoryObjet.creerObjet("redbull", joueur))
    l.deposerObjetAleatoirement(factoryObjet.creerObjet("clef", joueur))

# Ajouter des perroquets un peu partout
for i in range(50):
    l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("perroquet"))
    l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("singe"))

while True:  # Effacer la console
    cls()
    cls()
    joueur.printEnergie()
    print()
    l.afficher()
    print()

    # Afficher commandes dispo
    print("Que voulez vous faire ?")
    choix = input()
    actionManager.executer(choix)
    actionManager.afficherCommandesDispo()
    print()
    joueur.perdreEnergie()
    cls()
