#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

"""
Boucles :   while / for
Mots-clés : break (casse la boucle) / continue (revient au début de la boucle)
"""


#Boucle while
#-------------
#exemple 1
compteur = 0
while(compteur<5):
    print("je suis une phrase")
    compteur += 1
print("\nje suis sorti de la boucle")

#Exemple 2
jeu_lancé = True
while jeu_lancé:
        choixMenu = input(">")
        if choixMenu == "again":
            continue
        elif choixMenu == "quit":
            jeu_lancé = False
        elif choixMenu == "Hello":
            print("Bonjour :) !")
        else:
            print("Commande introuvable")

print("\nA bientôt")

#Boucle for
#Exemple 3
print("")
sentence ="Hello"
for letter in sentence:
    print(letter)

print("\nA bientôt")