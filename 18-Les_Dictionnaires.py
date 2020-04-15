#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

#Un tableau ressemble à un tableau associatif en php
#c'est comme une liste avec une clé

"""
Création de dictionnaire : dico = {}
                           dico = {<clé>:<valeur>,<clé2>:<valeur>}
Accès à une valeur       : dico[<clé>]
Ajout et modification au dictionnaire    : dico[<clé>] = <valeur>                            
Suppression              : dico.pop(<clé>)
                         : del dico[<clé>]
Copie de dictionnaire    : dico1 = {1:11,2:22}
                           dico2 = dico1.copy()
(_!_) Les clés sont uniques!                         
"""

#dico = {1:145,"prénom":"Liam"}
#print(dico)
#print(dico[1],dico["prénom"])
dico = {"Chat":"Siouxsie","Chien":"Le meilleur ami de l'homme"}
print(dico)
valeur_supprimée = dico.pop("Chien") #ou  del dico[{chien}]
print(valeur_supprimée)
if "chat" in dico:
    print("Oui")
else:
    print("Non")
print("")
dico = {"Chat":"Siouxsie","Chien":"Le meilleur ami de l'homme"}
for key in dico.keys():
    print(key)
for desc in dico.values():
    print(desc)
for k,v in dico.items(): #k et v est un tupe (k,v)
    print("La clé est : {} et la valeur est : {}".format(k,v))

#fonction
def maFonctionBizarre(**parametres):
    print(parametres)

maFonctionBizarre(p=54, nom="Blabla") 