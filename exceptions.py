"""
Ce fichier contient les définitions des exceptions définies pour ce projet.
Pour créer un nouveau type d'exception, il suffit d'hériter de la classe Exception, et de laisser le corps vide.
Ainsi la nouvelle exception récupère automatiquement les constructeur de la classe mère Exception
"""


class AbstractMethodCallException(Exception):
    """ Cette exception est levée lorsqu'on appelle une méthode abstraite.
    On ne doit normalement jamais les appeler puisqu'elles sont par définition redéfinies dans les classes filles
    des classes abstraites ou interfaces.
    """
    def __init__(self, classe ,method, message="The called method is an abstract one."):
        """
        Initialize the message.

        Args:
            self: (todo): write your description
            classe: (todo): write your description
            method: (str): write your description
            message: (str): write your description
        """
        self.classe = classe
        self.method = method
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        Return a string representation of this object.

        Args:
            self: (todo): write your description
        """
        return f"{self.method} in {self.classe} -> {self.message}"
