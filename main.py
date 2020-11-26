from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur

from objetFactory import ObjetFactoryPrincipale

from action import ActionManager
from personnesFactory import PersonnesFactoryPrincipale


import random
import keyboard


import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
input("   Appuyer sur 'Entrée' pour entrer dans le labyrinthe")


cls()

# Création des objets
# TODO: récupérer les attributs via un menu de configuration
joueur = Joueur.getInstance("X", 100)
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

# Ajouter des perroquets un peu partout
for i in range(50):
    l.deposerPersonneAleatoirement(factoryPersonne.creerPersonne("perroquet"))

while True:  # Effacer la console
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
