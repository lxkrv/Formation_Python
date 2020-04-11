#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

"""
Opérateurs de comparaion :  == (égal à)
                            != (différent de)
                            < (strictement inférieur)
                            > (strictement supérieur)
                            >= (supérieur ou égal)
                            <= (inférieur ou égal)

Conditions multiples :      and (ET)
                            or (OU)
                            in / not in (DANS / PAS DANS)
""" 

#Exemple 1
print("Exemple 1")
identifiant = "admin"
mot_de_passe = "password123"
print("interface de connexion")
user_id = input("Entrer votre identifiant : ")
user_password = input("Entrer votre mot de passe : ")
if user_password == mot_de_passe:
    print("Vous êtes connectés, bienvenue,", user_id)
print("Je ne suis plus dans le if")

#Exemple 2
print("\nExemple 2")
if user_password == mot_de_passe and user_id == identifiant:
    print("Vous êtes connectés, bienvenue,", user_id)
print("Je ne suis plus dans le if")

#Exemple 3
print("")
lettre_hasard = "b"
if lettre_hasard in user_id:
    print("b est dans l'identifiant")
else:
    print("b n'est pas dans l'identifiant")

#Exemple 4
print("")
age = input("tape ton age :")
if age == 18:
    print("tu viens d'être majeur")
elif age == 50:
    print("tu viens d'avoir 50 ans")
elif age == 60:
    print("tu viens d'avoir 60 ans")
else:
    print("tu as", age, "ans")

 #Exemple 5
jeu_chargé = True

if jeu_chargé:
     print("\nle jeu a été chargé")
else:
    print("\nle jeu a planté")

#Exemple 6
age = input("\nQUel âge as-tu? ")
age = int(age)

if age > 0 and age <= 100:
    print("l'âge est validé")
else :
    print("réponse incorrect")

#autre méthode pour l'exemple 6
"""age > 0 ET age <=100 --> 0 < age <= 100"""

if 0 < age <= 100:
    print("l'âge est validé")
else :
    print("réponse incorrect")