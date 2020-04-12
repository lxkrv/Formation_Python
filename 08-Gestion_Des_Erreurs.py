#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

"""
Gérer les exceptions    : try/except (+else,finally)

Types d'exceptions      : ValueError
                          NameError
                          TypeError
                          ZeroDivisionError
                          OSError
                          AssertionError


"""

"""
ageUtilisateur = input("Quel âge as-tu ? ")
try:
    ageUtilisateur = int(ageUtilisateur)
    print("tu as {} ans".format(ageUtilisateur))
except:
    print("L'âge indiqué n'est pas correct")
"""


"""
#version plus propre avec le else
ageUtilisateur = input("Quel âge as-tu ? ")
try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("L'âge indiqué n'est pas correct")
else:    
    print("tu as {} ans".format(ageUtilisateur))
finally:
        print("Fin du programme")
"""
"""
nombre1 = 15
nombre2 = input("choisir le dénominateur de la division : ")
try:
    nombre2 = int(nombre2)
    print("Résultat = {}".format(nombre1/nombre2))
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par 0")
except ValueError:
    print("Vous devez entrer un nombre")
except:
    print("valeur incorrect")
else:
    print("Bravo, tu sais taper un nombre!")
finally:
    print("Fin du programme...")
"""

"""
#Levée d'exception
try:
    age = input("Quel âge as-tu ? ")
    age = int(age)

    if age < 25:
        raise ZeroDivisionError("Coucou!")
except ZeroDivisionError:
    print("J'ai attrapé ton exception inutile")
"""

#Assert (c'est ce qu'on attend)
try:
    age = input("Quesl est ton âge ? ")
    age = int(age)

    assert age > 25 #Je veux que age soit plus grand que 25
except AssertionError:
    print("J'ai attrapé l'exception, l'age est inférieur à 25")