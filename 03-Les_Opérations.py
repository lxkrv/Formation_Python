#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

"""
Opérateurs en Python :  + (addition)
                        - (soustraction)
                        * (multiplication)
                        / (division)
                        % (modulo) -> rete d'une division euclidienne

variable = variable + X <--> variable += X                        
variable = variable - X <--> variable -= X
variable = variable * X <--> variable *= X
"""

calcul = 5 / 2
print("Résultat de type entier =",int(calcul))
print("Résultat de type entier =",float(calcul))
reste =  5 % 2
print("Le résultat est :",int(calcul),"et le reste (modulo 5%2) est",reste)

nombre = 14 % 2
print(nombre)

calcul1 = 5 + 3 * 7
calcul2 = (5 + 3) * 7
print(calcul1, calcul2)

niveauPersonnage = 1
print("Le niveau du personnage est ",niveauPersonnage)
print("Combat réussi, tu gagnes deux niveaux")
niveauPersonnage = 3
print("Le niveau du personnage est ",niveauPersonnage)

print("Combat réussi, tu gagnes un niveau")
niveauPersonnage = niveauPersonnage + 1
print("Le niveau du personnage est ",niveauPersonnage)