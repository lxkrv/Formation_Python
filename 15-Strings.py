#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

"""
une méthode de chaîne travaille sur une copie, et pas sur la chaîne elle-même.

str.upper(),str.lower,str.capitalize, str.title()
str.center(<largeur>,<caractère_remplissage>)
str.Strip()

str.find(<chaine>, <debut>, <occurence>)

str.isalpha(), str.isdigit(), str.isdecimal(), str.isnumeric(), str.isalphanum()

str.islowwer(),str.isupper()

str.isidentifier(), str.iskeyword()

"""
#Tout en Python est un objet

#help(str) permet de voir toutes les instructions

texte = "Hello World !" #Python voit ça comme une chaîne de caractère
print(texte)
print(texte.upper(),texte.lower(), texte.capitalize, texte.title()) 

#les méthodes travaillent sur une copie!
ch1 = "bonjour"
ch2 = ch1
print (ch1,ch2)
ch1 = ch1.upper()
print (ch1,ch2)

ma_chaine = "Mon Super Programme"
print(ma_chaine)
ma_chaine = ma_chaine.center(30,"-")
print(ma_chaine)

print(ma_chaine.find("Super"))
    
try:
    print(ma_chaine.index("super"))
except ValueError:
    print("Je n'ai pas trouvé cette chaîne")
ma_chaine2 = "     Mon Super Programme   "
print(ma_chaine.strip())
print(ma_chaine2.strip())

my_string = " ababababa"
print(my_string.replace("a","z",2))

phrase = "magicien|10|5"
print(phrase.split("|"))

print("")

ch = "Bonjour"
if ch.islower():
        print("Minuscule")
else:
    print("La chaine contient des majuscules")

ch = "class"
if ch.isidentifier():
    print("Réservé")
else:
    print("Libre")
print("")
if "Langage" in ch:
    print("Trouvé")
else:
    print("Pas là!")