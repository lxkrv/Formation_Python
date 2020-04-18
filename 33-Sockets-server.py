#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

"""
Socket logiciel différent de socket matériel!
les sockets sont apparus sur une distribution de la famille Unix (Berkeley) qui devaient permettre la communication entre machines sans se soucier de 
la manière dont est géré le réseau. Pas obligatoire d'avoir un réseau distant, on peut travailler sur la même machine.

mode tcp (connecté) établit une connexion et on peut communiquer. Les informations sont échangées et vérifiées

mode udp : plus rapide, les informations ne sont pas vérifiées (jeux en ligne, panneaux publicitaires)
""" 
import threading
class ThreadForClient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    
    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        print(data)

import socket

host, port = ('', 5566) #port choisi au hasard
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Le serveur est démarré...")

while True:
    socket.listen(5) #5 paramètre non obligatoire, nombre de connexion tenté avant de couper le serveur.
    conn, address = socket.accept()
    print("Un client vient de se connecter...")

    my_thread = ThreadForClient(conn)
    my_thread.start()

    
conn.close()
socket.close()
