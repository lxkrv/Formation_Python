#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import socket

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
   
    socket.connect((host, port))
    print("Client connecté !")
    data = "Bonjour Serveur, je suis le Client !:"
    data = data.encode("utf8")
    socket.sendall(data)
    
except: #ConnectionRefusedError (exemple d'erreur)
    print("Connexion au serveur échouée !")
finally:
        socket.close()

