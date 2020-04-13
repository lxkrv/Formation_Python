#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

"""
Propriété : manière de manipuler/contrôler des attributs
            principe d'enncapsulation
"""
"""
class Humain:
#Cette classe représente un humain

        def __init__(self, nom, age):
            print("Création d'un être humain...")
            self.nom = nom
            self._age = age #aide visuelle pour le développeur, pour savoir qu'on ne peut pas le modifier à l'extérieur

        def _getage(self):
            try:
            #print("Récupération non autorisée !")
                return self._age
            except AttributeError:  #Contrôle de l'accès
                print("L'âge n'existe pas !")
        
        def _setage(self, nouvel_age):
            if nouvel_age < 0:
                self._age = 0
            else:
                self._age = nouvel_age
        
        def _delage(self):
            del self._age


        #property(<getter>, <setter>, <deletter>, <helper>)       
        age = property(_getage, _setage, _delage, "Je suis l'âge d'un humain")

#Programme principal
Humain1 = Humain("John", 25)


print(Humain1.age)      #on passe par la propriété
Humain1.age = -5
print(Humain1.age)
del Humain1.age
print(Humain1.age) #va afficher que l'humain n'a plus d'attribut age
help(Humain)
print("")
help(Humain.age)
"""

class Humain:
#Cette classe représente un humain

        def __init__(self, nom, age):
            print("Création d'un être humain...")
            self.nom = nom
            self._age = age 

        def _getage(self):
            if self._age <= 1:
                return str(self._age) + " an"
            return str(self._age) + " ans"
            
        
#property(<getter>, <setter>, <deletter>, <helper>)       
        age = property(_getage)

#Programme principal
Humain1 = Humain("Jim", 15)
Humain2 = Humain("Tchio",1)
print("")
print("{} a {}".format(Humain1.nom,Humain1.age))
print("")
print("{} a {}".format(Humain2.nom,Humain2.age))