import random
import time
import os

def clear():
    os.system("clear")

def playerstats():
    print(f"\nStatus            Vida: {vid} Ataque: {ata} Cura: {cur}")


def inistats():
    print(f"Inimigo           Vida: {inivid} Ataque: {iniata}")

def welcome():
    print("\n ?????   ???   ?????                    ?????                           ????")
    print(" ????   ????   ????                     ??????                          ??? ")
    print(" ????   ????   ????  ??????   ???????   ????   ??????   ???????        ???? ")
    print(" ?????  ?????  ???   ???????  ????  ??  ????    ??????  ???? ???? ???  ???? ")
    print("  ???????????????   ????????  ????      ????  ????????  ???? ???? ???  ???? ")
    print("    ????? ?????    ???   ???? ????      ???? ???   ???? ???? ???? ???  ?????")
    print("     ???   ???      ???????? ?????     ?????  ???????? ???? ?????  ???????? ")
    input("\n                           Press ENTER to Start")
    clear()

welcome()

#Herois-------------------------------------------------------------------------
print("\n1 - Cavaleiro")
print("2 - Arqueiro")
print("3 - Mago")
print("4 - Assasino")
print("5 - Clérigo")
print("6 - Paladino")
print("7 - Bárbaro")
print("8 - Necromante")
print("9 - Druida")
print("10 - Monge")
char = eval(input("\nEscolha sua classe: "))
clear()

if char == 1:
    vid = 150
    ata = 15
    cur = 10
    print("\nVocê escolheu Cavaleiro")

elif char == 2:
    vid = 90
    ata = 20
    cur = 5
    print("\nVocê escolheu Arqueiro")

elif char == 3:
    vid = 90
    ata = 25
    cur = 15
    print("\nVocê escolheu Mago")
elif char == 4:
    vid = 100
    ata = 20
    cur = 5
    print("\nVocê escolheu Assassino")

elif char == 5:
    vid = 150
    ata = 15
    cur = 20
    print("\nVocê escolheu Clérigo")
elif char == 6:
    vid = 150
    ata = 15
    cur = 15
    print("\nVocê escolheu Paladino")

elif char == 7:
    vid = 120
    ata = 20
    cur = 5
    print("\nVocê escolheu Bárbaro")
elif char == 8:
    vid = 100
    ata = 15
    cur = 10
    print("\nVocê escolheu Necromante")

elif char == 9:
    vid = 100
    ata = 10
    cur = 15
    print("\nVocê escolheu Druida")
elif char == 10:
    vid = 120
    ata = 10
    cur = 20
    print("\nVocê escolheu Monge")
time.sleep(1)
clear()

#inimigo Aleatorio--------------------------------------------------------------
print("\nVocê enfrentará um inimigo aleatório, prepare-se!")
time.sleep(1)
clear()

#inimigo Aleatorio--------------------------------------------------------------
ini = (random.randint(1, 3))

#inimigos-----------------------------------------------------------------------
if ini == 1:
    inivid = 80
    iniata = 5
    print("\nSeu inimigo é um Goblin")

elif ini == 2:
    inivid = 90
    iniata = 5
    print("\nSeu inimigo é um Zumbi")

elif ini == 3:
    inivid = 100
    iniata = 5
    print("\nSeu inimigo é um Esqueleto")
elif ini == 4:
    inivid = 100
    iniata = 10
    print("\nSeu inimigo é um Harpia")
elif ini == 5:
    inivid = 100
    iniata = 15
    print("\nSeu inimigo é um Bruxa")
elif ini == 6:
    inivid = 120
    iniata = 10
    print("\nSeu inimigo é um Múmia")
elif ini == 7:
    inivid = 130
    iniata = 15
    print("\nSeu inimigo é um Minotauro")
elif ini == 8:
    inivid = 140
    iniata = 15
    print("\nSeu inimigo é um Ciclope")
elif ini == 9:
    inivid = 150
    iniata = 15
    print("\nSeu inimigo é um Retalhador")
elif ini == 10:
    inivid = 200
    iniata = 20
    print("\nSeu inimigo é um Ceifero")
time.sleep(1)
clear()

#Combate------------------------------------------------------------------------
while (vid > 0 and inivid > 0):
    playerstats()
    inistats()
    print("\nSua Vez:")
    print("1 - Atacar")
    print("2 - Curar")
    esc = eval(input("Escolha: "))
    clear()
    
    if esc == 1:
        inivid -= ata
        
    elif esc == 2:
        vid += cur
        
    
    print("\nvez do inimigo")
    time.sleep(1)
    vid-= iniata
    
    clear()
    print(f"\nInimigo ataca com {iniata} de dano")
    
    if inivid <=0:
        clear()
        print("\nVocê Ganhou!")
        time.sleep(1)
    elif vid <=0:
        clear()
        print("\nVocê Perdeu!")
        time.sleep(1)
