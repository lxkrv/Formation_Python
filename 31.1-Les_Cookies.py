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
httponly: pour empêcher que le coockie soit exploitable depuis du javascript

Set-Coockie: pref_lang=fr; httponly
"""
import cgi
import http.cookies
import datetime
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # on récupère le descripteur et on modifie l'encodage de la sortie standard

print("content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset = utf-8>
    <title>Ma page web</title>
</head>
<body>
    <h1>Coockies avec Python</h1>
"""
print(html)
try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print("La langue utilisée par l'utilisateur est : ",user_lang["pref_lang"].value)
except(http.cookies.CookieError, KeyError):
    print("Non trouvé")


html = """
</body>
</html>
"""
print(html)
