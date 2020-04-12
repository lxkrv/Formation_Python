#coding:utf-8


def parler(personnage, message):
    print("{} : {}".format(personnage, message))

def au_revoir():
    print("Au revoir!")


#eProcédure de test
if __name__ == "__main__":
    print("Phase de test")
    parler("Jason","Bonjour tout le monde")
