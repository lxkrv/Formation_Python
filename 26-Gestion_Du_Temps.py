#coding:utf-8
import os
import time #--->objet du cours
# for windows
os.system('cls')
#os.system("ls")

"""
time.sleep()  
    .time()
    .localtime()
    .mktime()
    .strftime()
"""


print("Le premier texte")
time.sleep(0.5)
print("Le second texte")

#1er janvier 1970 à 00h00
print(time.time())

begin = time.time()
print("Début")
time.sleep(3)

end = time.time()
print("Fin")

print(f"Temps d'exécution : {end - begin} s")
print("")
print(time.localtime())
print("")
"""
            localtime()
(TIMESTAMP)-------------> structure de temps
           <-------------
             mktime()
"""
tps = time.localtime()
print(tps)
tps = time.mktime(tps)
print(tps) 
print("")
"""
%d : jour (01-->31)
%m : mois (01-->12)
%Y : année (ex : 2018) - %y (00-->99)
%H : heure (00-->23)
%I : minute (00-->59)
%s : seconde (00-->59)

%A : jour semaine / %a (jour abrégé)
%B : mois / %b (mois abrégé)

%Z : fuseau horaire (timezone)
"""

my_time = time.strftime("%A")
print(my_time)
my_time = time.strftime("%d/%m/%Y")
print(my_time)