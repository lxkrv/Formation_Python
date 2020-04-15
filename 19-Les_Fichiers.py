#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

"""
Mode d'ouverture : r (lecture seul)                             +
                   w (écriture avec remplacement)               +
                   a (écriture avec ajout en fin de fichier)    +
                   x (lecture et écriture dans un même fichier) -
                   r+ (lecture/écriture dans un même fichier)   -

Lecture           : read(), readline(), readline()

Tout ce qui va être traîté, va être traité comme une chaîne de caractères
"""

fic = open("Données.txt","r") # si dans un répertoire, doc/données.txt

#print(fic.read())
content = fic.read()
print(content)

"""
line = fic.readline()
print(line)
line = fic.readlines()  #récupère sous forme de liste
print(line)
"""

fic.close()
if fic.closed:
    print("Fichier fermé")
else:
    print("Fichier encore ouvert")

with open("Données.txt", "r") as fic: #pas besoin de fermer avec cette méthode, dans le with, le fichier reste ouvert
        content = fic.read()
        print(content)

with open("Données2.txt", "w") as fic:
    nombre = 15
    fic.write(str(nombre))
    fic.write("\nBonjour, je suis une phrase\n")
    fic.write("Et une autre")

import pickle

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def whoami(self):
        print("{} ({})".format(self.name, self.level))

#Player1 = Player("John", 10)
"""
with open("Player.data", "wb") as fic:
    record = pickle.Pickler(fic)
    record.dump(Player1)
"""
with open("Player.data", "rb") as fic:
    record = pickle.Unpickler(fic)
    Player1 = record.load()

Player1.whoami()