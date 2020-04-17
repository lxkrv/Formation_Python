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




print("Content-type : text/html; charset=utf-8\n")
html = """<!Doctype html>
<head>
    <meta charset="UTF-8">
    <title>Une page web avec Python</title>
</head>
<body>
    <h1>Bienvenue</h1>
    <p>Je suis en Python, avec une page Web avec Python et HTML</p>
    <p>Blah blah</p>
</body>
</html>
"""
print(html)
print("<h1>Hello</h1>")