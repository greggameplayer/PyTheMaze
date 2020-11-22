from personnesFactory import PersonnesFactory,PersonnesFactoryPrincipale
from personnes.perroquet import Perroquet
import random
class perroquetFactory(PersonnesFactory):

    def creerInstance(self):
        couleur = random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])
        return Perroquet(couleur)

PersonnesFactoryPrincipale.getInstance().registerFactory("perroquet", perroquetFactory())