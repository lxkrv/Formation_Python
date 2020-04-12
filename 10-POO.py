"""
------------------------------------------------------------
La programmation orientée objet (POO) avec le langage Python
------------------------------------------------------------

- Afficher du texte
- Saisir des informations
- Variables
- Conditions et boucles
- Fonctions et modularités
- Gestion des erreurs

classe              : plan de conception, genre (exemple: Humain)
Objet               : instance de classe (exemple: Julien)

Attribut            : c'est une variable de classe (exemple : prénom, age, poids, taille,...)
Propriété           : la différence est pratiquement invisible avec l'attribut, la propriété est le moyen de manipuler des attributs (lecture seule, accès non autorisé en dehors de la classe, etc...)

Méthode             : fonction d'une classe (exemple: manger(nourriture,quantité), marcher, parler, dormir)
Méthode de classe   : fonction d'une classe (explications à venir plus tard...)
Méthode statique    : fonction d'une classe, mais indépendante de celle-ci

Héritage            : classe Fille qui hérite d'une classe Mère (Fille est une sorte de Mère)
                    : classe Chat hérite de la classe Animal (Chat est une sorte d'Animal)
"""
#Exemple, méthode format
nom = "John"
test = "Bienvenue {} ".format(nom)

print(test)
