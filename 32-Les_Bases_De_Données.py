#coding:utf-8
import os
# for windows
os.system('cls')
#os.system("ls")

#CRUD : Create, Read, Update, Release

"""
SQlite est fait pour remplacer l'utilisation de fichier texte et pas autre chose. conçu pour fonctioner depuis le téléphone.
On ne doit pas utiliser SQListe si on doit gérer une grosse quantité de données (> 1Go)
Connexion unique sur la base de données

connection multiple et >1 go, mysql
1To -->postGre
"""
import sqlite3

try:
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    req2 = cursor.execute('SELECT * FROM t_users')
#print(req2.fetchall())

    for row in req2.fetchall():
        print("-",row[1],"-")

except Exception as e:
    print("[ERREUR] : ",e)
    connection.rollback()

finally:
    connection.close()





#print(type(connection))
#print(type(cursor))

"""
#Lecture dans la base
my_username = ("John", )
cursor.execute('SELECT * FROM t_users WHERE user_name = ?',my_username)
result = cursor.fetchone()[1]

print(f"Le nom d'utilisateur est : {result}")
"""
"""
#Ecriture dans la base
new_user = (cursor.lastrowid, "Alex", 41)
cursor.execute('INSERT INTO t_users VALUES(?,?,?)', new_user)
connection.commit()
print("Nouvel utilisateur ajouté !")
"""