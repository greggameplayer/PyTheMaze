from configMenu import ConfigMenu
from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur

from objetFactory import ObjetFactoryPrincipale

from action import ActionManager
from personnesFactory import PersonnesFactoryPrincipale

import os, sys



def cls():
    """
    Return the system class.

    Args:
    """
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

difficultyChoice = int(ConfigMenu().ask())

if difficultyChoice == 1:
    joueur = Joueur.getInstance("👤", "X", 70)
    monsterSpawnRate = 2
    potionRate = 40
    redbullRate = 20
    l = Labyrinthe.getInstance(20, 10)
elif difficultyChoice == 2:
    joueur = Joueur.getInstance("👤", "X", 60)
    monsterSpawnRate = 4
    potionRate = 30
    redbullRate = 15
    l = Labyrinthe.getInstance(30, 20)
else:
    joueur = Joueur.getInstance("👤", "X", 55)
    monsterSpawnRate = 8
    potionRate = 25
    redbullRate = 10
    l = Labyrinthe.getInstance(30, 30)

l.deposerJoueurAleatoirement(joueur)
factoryObjet = ObjetFactoryPrincipale.getInstance()
factoryObjet.loadFactoryPlugins()
factoryPersonne = PersonnesFactoryPrincipale.getInstance()
factoryPersonne.loadFactoryPlugins()
actionManager = ActionManager.getInstance()
actionManager.loadActionPlugins()

# Generation de 35 potions aléatoirement
for i in range(potionRate):
    l.deposerObjetAleatoirement(factoryObjet.creerObjet("potion"), joueur)

for i in range(redbullRate):
    l.deposerObjetAleatoirement(factoryObjet.creerObjet("redbull"), joueur)

for i in range(12):
    l.deposerObjetAleatoirement(factoryObjet.creerObjet("clef"), joueur)

# Ajouter des perroquets un peu partout
for i in range(15):
    l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("perroquet"), joueur)
for i in range(10):
    l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("clown"), joueur)
for i in range(monsterSpawnRate):
    l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("singe"), joueur)
    l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("crocodile"), joueur)

l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("sphinx"), joueur)
l.deposerObjetAleatoirement(factoryObjet.creerObjet("crane"), joueur)
l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("indiana"), joueur)


while True:  # Effacer la console
    cls()
    if joueur.energieChecker():
        break
    actionManager.jouer()
