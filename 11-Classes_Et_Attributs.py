#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)
"""
classe              : plan de conception, genre (exemple: Humain)
Objet               : instance de classe (exemple: Julien)
Attribut            : c'est une variable de classe (exemple : prénom, age, poids, taille,...)
"""
#premier exemple
"""
class Humain:       #Constructeur

       def __init__(self): # le self c'est ce qui cible l'objet, le constructeur va rendre self, donc l'objet
        print("Création d'un humain...", self) #self, c'est juste pour l'avoir l'adresse quand on crée l'humain
        self.prenom = "Jojo"
        self.age = 1
        pass

print("Lancement du programme...")

humain1 = Humain()
print("Prénom de l'humain n°1 : {} ".format(humain1.prenom))
humain2 = Humain()
"""
"""
#Exemple 2

class humain:       
    def __init__(self, c_prenom, c_age=999): #999 valeur par défaut si on ne passe pas de paramètre à la création
        print("Création d'un humain...") 
        self.prenom = c_prenom
        self.age = c_age

print("Lancement du programme...\n")

humain1 = humain("Jojo")
print("Prénom de l'humain n°1 : {}".format(humain1.prenom))
print("Age de l'humain n°1 : {}".format(humain1.age))
print("")
humain2 = humain("Jonsi", 74)
print("Prénom de l'humain n°1 : {}".format(humain2.prenom))
print("Age de l'humain n°1 : {}".format(humain2.age))

humain1.prenom = "Bill"
print("\nChangement du prénom de l'humain n°1 : {}".format(humain1.prenom))
"""

class humain:
    humains_crees = 0       #Attention à bien mettre dans la classe
    def __init__(self, c_prenom, c_age): 
        print("Création d'un humain...") 
        self.prenom = c_prenom
        self.age = c_age
        humain.humains_crees += 1 #!!pas de self, la variable appartient ) la classe


print("Lancement du programme...\n")

humain1 = humain("Luc", 12)
print("Nombre d'humains créés : {}".format(humain.humains_crees))

humain2 = humain("Phil", 21)
print("Nombre d'humains créés : {}".format(humain.humains_crees))