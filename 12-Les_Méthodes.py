#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

"""
Méthode             : fonction sur une instance (objet)
Méthode de classe   : fonction sur une classe 
Méthode statique    : fonction indépendante mais "liée" à une classe
"""

class Humain:
    """Classe qui définit un humain"""
    Lieu_Habitation = "Terre"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def Parler(self, message):                  #self = méthode standard
        print("{} a dit : {}".format(self.nom, message))

    def Changer_Planète(cls, Nouvelle_Planète): #cls = méthode de classe
        Humain.Lieu_Habitation = Nouvelle_Planète

    C_P = classmethod(Changer_Planète) #-->Ligne  importante, attention à l'indentation

    def Definition():                  #Méthode statique
            print("L'humain est classé comme étant une grosse buse !")
    Definition = staticmethod(Definition)


#Programme principal


Humain1 = Humain("John",35)
Humain1.Parler("Hello world !")
Humain1.Parler("Comment ça va ?")

print("")

print("La planète actuelle est : {}".format(Humain.Lieu_Habitation))
Humain.C_P("Mars")
print("La planète actuelle est : {}".format(Humain.Lieu_Habitation))

print("")

Humain.Definition()