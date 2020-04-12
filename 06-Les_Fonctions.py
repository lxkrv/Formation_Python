#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

"""
Résumé :
--------
Fonctions vues :    print(),input()
                    type(),int(),float(),str(),bool()

Une fonction ne sert qu' à une seule chose!!
"""     

print("Hello everybody!")
age = input("Quel âge as-tu?")
age = int(age)
print("tu as {} ans.".format(age))
#----------------------------------------
#Fonction sans paramètre
def dire_bonjour():
    print("Hello!")
#je ne suis plus dans la fonction

dire_bonjour()
#------------------------------------
#Fonction avec paramètres
def dire(nom_personne, message_personne):
    print("{} : {}".format(nom_personne, message_personne))
print("")
dire("John","Hello")
dire("Bill","Goodbye")

#Fonction avec paramètres optionnels
def dire1(nom_personne="Tom", message_personne="Salut"):     #Paramètre optionnel!
    print("{} : {}".format(nom_personne, message_personne))
print("")
dire1()
dire1("Bill","Goodbye")

#Fonction avec paramètres optionnels
def dire2(nom_personne = "Tom", message_personne = "Salut", age_personne = 18):     #Paramètre optionnel!
    print("{} : {} ans : {}".format(nom_personne, age_personne, message_personne))
dire2("yo!",25, "Roger")
dire2(nom_personne = "Yeah", age_personne = 25, message_personne = "Hey gros!")
dire2(nom_personne = "David",age_personne = 12)

#-----------------------------------------------
def show_inventory(*list_items):
    for item in list_items:
        print(item)

print("")
show_inventory("épée")
print("")
show_inventory("épée","arc","potion de mana","cape de Dragon rouge")

#fonction qui retourne une valeur
def calculer_somme(nombre1,nombre2):
    résultat = nombre1 + nombre2
    return résultat                 #on peut retourner qu'un élément, le return quitte la fonction

print(calculer_somme(5,3))

def le_plus_grand(nombre1,nombre2):
    if nombre1 > nombre2:
        return nombre1
    elif nombre1 < nombre2:
        nombre2 > nombre2
        return nombre2
    else:
        return "Egalité"

print(le_plus_grand(4,4))

#--------------------------------
"""
print("1. Faire une somme")
print("2. Faire une différence")
print("3. Quitter le programme")


print("1. Faire une somme")
print("2. Faire une différence")
print("Faire une multiplication")
print("4. Quitter le programme")

il vaut mieux créer une fonction menu
def menu()
    print("1. Faire une somme")
    print("2. Faire une différence")
    print("Faire une multiplication")
    print("4. Quitter le programme")
"""

#--------------------------------------------------
#la fonction lambda, elle peut prendre des paramètres ou non. Elle va faire le retour d'une instruction
lambda: print("bonjour")
#--> Equivalent à 
#def lambda:
#    print("Bonjour")

coucou = lambda:(print("bonjour"))
print("coucou\n")
#-----------------------------
TTC = lambda prixHT:prixHT + (prixHT * 20 / 100)
print(TTC(24))
#------------------------------
calculer = lambda a,b : a + b
print("\n",calculer(10,5))