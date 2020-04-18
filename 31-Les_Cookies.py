#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")


"""
Les coockies sont des fichiers textes que le navigateur va enregistrer et qui permet de stocker une information.
Un coockie va porter un nom, contenir uen valeur, une période de validité. Pas d'identifiant, ni de mot de passe, le
coockie stocke des préférences utilisateurs par exemple.

"""

"""
L'entête du coockie doît être générée avant de charger du HTML

expires : date d'expiration du coockie Sat, jj-mm-yy 12:45:17 (UTC optionnel)
path : chemin du coockie
comment : commentaire de coockie
domain  : racine du site
max-age : attention, pas compatible avec tous les navigateurs (à éviter)
secure  : pour que le coockie fonctionne sur une connexion HTTPS
version : version du coockie
httponly: pour empêcher que le coockies soit exploitable depuis du javascript

Set-Coockie: pref_lang=fr; httponly
"""
import cgi
import http.cookies
import datetime

création du cookie
expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%Ss")

my_cookie = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"]["httponly"] = True


print("Set-Coockie: pref_lang=fr; httponly") #A mettre en premier
print("content-type: text/html; charset=utf-8\n")
print(my_cookie.output())
html = """<!DOCTYPE html>
<head>
    <meta charset = utf-8>
    <title>Ma page web</title>
</head>
<body>
    <h1>Coockies avec Python</h1>
"""
print(html)
print("<p>Bonjour !</p>")

html = """
</body>
</html>
"""
print(html)
