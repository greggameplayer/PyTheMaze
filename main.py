from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur

from objets.potion import Potion
from personnes.perroquet import Perroquet

from action import ActionManager

import random


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
l = Labyrinthe(20,10)
joueur = Joueur("X",100)
l.deposerJoueurAleatoirement(joueur)

# Generation de 70 potions aléatoirement
for i in range(70):
    potion = Potion(random.randint(5,10))
    l.deposerObjetAleatoirement(potion)

# Ajouter des perroquets un peu partout
for i in range(50):
    l.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))




# Gestion des actions
actionManager = ActionManager.getInstance()
actionManager.loadActionPlugins()

while True:
    cls()  # Effacer la console
    joueur.printEnergie()
    print()
    l.afficher()
    print()


    # Afficher commandes dispo
    print("Que voulez vous faire ?")
    actionManager.afficherCommandesDispo()
    # Récupérer entrée utilisateur
    choix = input("Que dois-je faire ? ")

   # Exécuter la commande
    actionManager.executerEntreeUtilisateur(choix)














    else:
        print("Moi pas comprendre...")
        print("Mon vocabulaire est limité  à n, s, e, o, regarder, ramasser, sac et parler.")
        input()

    joueur.perdreEnergie()
