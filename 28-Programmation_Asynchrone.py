#coding:utf-8
import os
import time #--->objet du cours
# for windows
os.system('cls')
#os.system("ls")

import threading

my_lock = threading.RLock()


class MyProcess(threading.Thread):
    def __init__(self):
       threading.Thread.__init__(self)

    def run(self):
        i = 0
        while i < 3:
            with my_lock: #verrou/ on verra ABCABC dans l'ordre
                letters = "ABC"
                for lt in letters:
                    print(lt)
            #print(threading.current_thread()) #pour exemple 1
            time.sleep(0.25) 
            i += 1
"""Pour excemple 1
def process_one():
    i = 0
    while i < 3:
        print("oooOOOooo")
        time.sleep(0.25)
        i += 1

def process_two():
    i = 0
    while i < 3:
        print("xxxXXXxxx")
        time.sleep(0.5)
        i += 1

"""
#process_one()
#process_two()


th1 = MyProcess()
th2 = MyProcess()

th1.start()
th2.start()

th1.join()
th2.join()

print("Fin du programme")