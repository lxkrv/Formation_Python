#coding:utf-8

import cgi
import cgitb

cgitb.enable()    #activation du mode debug (en developpement, jamais quand le site est en ligne)
form = cgi.FieldStorage()

print("content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset = "utf-8">
    <title>Une page web avec Python</title>
</head>
<body>
"""
print(html)

try :
    if form.getvalue("username"):
        username = form.getvalue("username")
        print(f"Bonjour {username} !")
        print("<script>alert('OK')</script>")
    else:
        raise Exception("Pseudo non valide")
except:
    print("Pseudo non transmis")

html = """
</body>
</html>
"""
print(html)
