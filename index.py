#coding:utf-8
import os
import time #--->objet du cours
# for windows
os.system('cls')
#os.system("ls")

import cgi
"""
Limitation du cgi, il va démarrer une requête à chaque actualisation.Sur des grosses applications, ce n'est pas très optimisé.
On est passé sur du FAST CGI
"""

print("content-type: text/html; charset=utf-8\n")
    
html = """<!DOCTYPE html>
<head>
    <meta charset = utf-8>
    <title>Ma page web</title>
</head>
<body>
    <h1>Page web avec Python CGI</h1>

    <form methode = "post" action = "result.py">
    <p><input type = "text" name = "username">
    <input type = "submit" value = "Envoyer"></p>
    </form>
</body>
</html>
"""
print(html)
