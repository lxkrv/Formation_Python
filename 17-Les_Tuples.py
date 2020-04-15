#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

"""
Un tuple est immuable, on peut le créer, mais on ne peut plus le modifier par la suite
Création de tuple : mon_tuple = () #vide
                    mon_tuple = (17,) ou mon_tuple = 17, une seule valeur
                    mon_tuple = (45,12) #plusieurs valeurs 

Le tuple peut servir de constante. On peut y accéder []
Accés au tuple : mon_tuple[x] #valeur d'indice X
(!) Tuple : conteneur immuable (conteneur dont on ne peut modifier les valeurs)
2 raisons d'utiliser des tuples : affectations multiples de variables
                                  retour multiple de fonction
"""


liste = [1,2,3,4,5,6]
for chose in enumerate(liste):
    print(chose)

mon_tuple =()
print(type(mon_tuple))

mon_tuple =(45) #--> pas un tuple
print(type(mon_tuple))

mon_tuple =(45,) #c'ets un tuple
print(type(mon_tuple))
print(mon_tuple[0])

mon_tuple2 = (45,64)
try:
    print(mon_tuple[2])
except:
    print("Dépassement du tuple")

nombre1 = 14
nombre2 = 46
(nombre1,nombre2) = (14,46)
print(nombre1, nombre2)

nombre1 = 128
print(nombre1)

def get_position_joueur():
    posX = 148
    posY = 86
    return (posX, posY) #on retourne un tuple qui contient les valeurs
#programme principale
print("" )
coordX = 0
coordY = 0
print("Position du joueur : ({}/{})".format(coordX,coordY))
(coordX, coordY) = get_position_joueur()
print("Position du joueur : ({}/{})".format(coordX,coordY))