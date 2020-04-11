#coding:utf-8

"""
Nommer une variable :   doit commencer par une lettre
                        ne doit pas contenir de caractère spéciaux
                        ne pas contenir d'espaces
                        utilisers des underscores(_)

Types standards :       entier(int)
                        nombre flottant(float)
                        chaîne de caractères(str)
                        booléen (bool)                        
"""
"""
agePersonne
age_personne
agePersonneAge_Personne #exemplage de nommage
_AgePersonne
"""
PrixHt = 14.5 #type entier"
age = 14            #typage dynamique
Variable_booléenne = True
Age_Personne = "25" #chaîne de caractères

print(Age_Personne,"est une variable de type",type(Age_Personne))

text = "L'age de la personne est {} et le prix HT est de {} $"
print(text.format(age, PrixHt))
print("L'age de la personne est {} et le prix HT est de {} $".format(age, PrixHt))

#Fonction vues : print()                    -> Affiche à l'écran
#                input()                    -> lire au clavier
#                type()                     -> retourne le type d'une donnée, variable, etc..
#                str.format()               -> formater une chaîne
#                int(),float, str(), bool() -> "caste" une donnée, la convertit

Nom_Joueur = input("Quel est ton nom : ")
print("Bienvenue", Nom_Joueur)

Prix_HT = input("quel est le prix : ")
Prix_TTC = float(Prix_HT)*1.2

print("le prix TTC est  : ", Prix_TTC)

Valeur_Booleen = False
Valeur_Booleen = str(Valeur_Booleen)
print(Valeur_Booleen)