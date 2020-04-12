#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)
"""
Import un module :  import <nom_du_module>
                    from <nom_du_module> import *
un module est un fichier
"""                    

"""
import math

on peut faire aussi
from match import sqrt

resultat = math.sqrt(100)
print(resultat)

from math import sqrt
from math import sinus

resulat = sqrt(100)
sinus = math.sin(42)
"""
#Première façon de faire
#import Player
#Player.au_revoir()
#Player.parler("John","Bonjour tout le monde!")

#deuxième façon de faire
"""
from Player import au_revoir
from Player import parler
au_revoir()
parler("John","Bonjour tout le monde!")
"""
#avec un chemin pour le module
"""
import Includes.Player
Includes.Player.au_revoir()
Includes.Player.parler("John","Bonjour tout le monde!")
"""
import Includes.Player as player
player.au_revoir()
player.parler("John","Bonjour tout le monde!")
