#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

#Création d'un liste
"""
liste[X] = Affiche élément d'indice X
liste[-X] = affiche Xème élement en partant de la fin
liste[:] = affiche tous les éléments
liste[:X] = Affiche les X premiers éléments
liste[X:] = Affiche les X derniers éléments
liste[A:B] =  Affiche de l'élément d'indice A à l'élément B (exclus)

len(<list>) = Retourne la taille (nombre d'éléments)
"""

"""
inventaire = list()
ou
inventaire = [] #autre méthode pour créer une liste vite
inventaire = [1,2,15]

inventaire = [88]*10

inventaire = range(20)
i = 0
while i < len(inventaire):
    print(inventaire[i])
    i+=1

print(inventaire)
print(type(inventaire)) 
"""
inventaire = ["arc", "épée","bouclier","potion","flèches","tunique"]
for valeur in inventaire:
    print(valeur)
print("")
print(inventaire[1]) #affiche l'élément 1
print(inventaire[:2]) #affiche les deux premiers éléments
print(inventaire[2:]) #affiche les éléments moins les deux premiers

print(inventaire[-4]) #affiche le 4eme élément à partir de la fin
print(inventaire[2:4])

print("")
print(inventaire[:])
inventaire[:2] = "bouclier d'acier"
print(inventaire[:])

if "bouclier" in inventaire:
    print("je possède un bouclier")
else:
    print("pas de bouclier!")

print("")

inventaire = ["arc", "épée","bouclier","potion","flèches","tunique"]
inventaire.append("slip") # entre nouvel élémentn en fin de liste
print(inventaire)

inventaire.insert(1,"casque") #insert l'élément ) l'indice
print(inventaire)

#suppression du slip
print("Suppression du slip")
inventaire.remove("slip")
print(inventaire)

print("")
#suppression d'un objet, on peut aller plus vite avec le remove()
index = inventaire.index("bouclier")
del inventaire[index]
print(inventaire)

tri = inventaire.sort()#trier dans l'ordre croissant, reverse() décroissant
print(tri)
print("")
liste1 =["épée","potion","bouclier","potion","casque"]
print("Nombre de potions : ",liste1.count("potion"))

#effacement de liste :
inventaire.clear()
print(inventaire)
liste1[:] = []
print(liste1)

chaine = "Hello world !" #attention marche pas avec des entiers!
chaine2 = chaine.split()
chaine3 = "_".join(chaine2)
print(chaine3)


#####################""""""
liste1 = ["Epée","Bouclier","Casque"]
liste2 = liste1
print("Liste 1 :", liste1[:])
print("Liste 2 :", liste2[:])

liste2.append("Slip")

print("Liste 1 :", liste1[:]) #l'ajout a été fait sur la liste 1
print("Liste 2 :", liste2[:])
#######Autre méthode#######################"
import copy
liste1 = ["Epée","Bouclier","Casque"]

#ne fais pas de copie
liste2 = copy.deepcopy(liste1) 
print("Liste 1 :", liste1[:])
print("Liste 2 :", liste2[:])

liste2.append("Slip")

print("Liste 1 :", liste1[:]) #l'ajout a été fait sur la liste 1
print("Liste 2 :", liste2[:])

#ajout d'une liste à une autre
liste1 = ["Epée","Bouclier","Casque"]
liste2 = ["Potion","Tunique"]

liste1.extend(liste2)
#ou liste1 = liste1 + liste2
print(liste1)

for objet in enumerate(liste1): #va créer un tuple, possibilté de récupérer l'indice
    print(objet)

print("")
for indice_objet, valeur_objet in enumerate(liste1):
    print("Elément d'indice : {} -> {}".format(indice_objet, valeur_objet))