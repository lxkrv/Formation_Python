#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

#Classe mère
class Vehicule:
    def __init__(self, nom, quantite_essence):
        self.nom = nom
        self.essence = quantite_essence

    def montrer_vehicule(self):
        return self.nom
    
    def se_deplacer(self):
        print("Le véhicule {} se déplace...".format(self.nom)) #-->héritage de la classe

#Classe fille
class Voiture(Vehicule):
    #pas besoin ici de recréer une méthode
    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self,nom_voiture, essence)
        self.puissance = puissance
    
    def se_deplacer(self):
        print("Je roule...")

#Premier exemple - créer de la même manière qu'avant
v1 = Vehicule("Falcon", 2400)
v2 = Vehicule("Toyota Yaris", 45)
print(v1.nom)
print(v2.nom)
"""
"""
class Avion(Vehicule):
    def __init__(self, nom, essence, marchandise):
        Vehicule.__init__(self, nom, essence,)
        self.marchandise = marchandise
    
    def se_deplacer(self):
        print("Je vole...") # on peut redéfinir la méthode

class Voiture_Sport(Voiture):
    pass

#Programme principal
voiture1 = Voiture("Toyota Yaris", 55, 120)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")

print("")
av1 = Avion("F22 Raptor", 2400, 420)
av1.se_deplacer()


#utilité de l'héritage : pour éviter la répétition de code, hiérarchie au niveau des classes
"""
fonctions utiles :
    isinstance(<objet>,<classe>) : vérifie qu'un objet est de la classe renseignée
    issubclass(<classe_fille>,<classe_mère>) : vérifie qu'une classe est fille d'une autre

"""
class Animal:
    def __init__(self, nom):
        self.nom = nom
    def manger(self):
        print(self.nom, "mange...")

class Reptile(Animal):
    def __init__(self, nom, regime_alimentaire):
        Animal.__init__(self, nom)

#Code principale
lezard = Reptile("Lézard", "grenouilles")
lezard.manger()
print("")
print(isinstance(lezard,Animal)) 
if isinstance(lezard, Reptile):
    print("Lezard est un animal")
#Une classe fille est toute la classe mère plus autre chose
if issubclass(Reptile, Animal):
    print("Reptile hérite d'animal")