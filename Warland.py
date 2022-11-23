import random
import time
import os

def clear():
    os.system("cls")

def playerstats():
    print(f"\nStatus            Vida❤️: {vid} Ataque⚔️: {ata} Cura✚: {cur}")


def inistats():
    print(f"Inimigo           Vida❤️: {inivid} Ataque⚔️: {iniata}")

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

def loading():
    clear()
    print("\nvez do inimigo ⌛")
    time.sleep(0.3)
    clear()
    print("\nvez do inimigo ⏳")
    time.sleep(0.3)    
    clear()
    print("\nvez do inimigo ⌛")
    time.sleep(0.3)   
    clear()
    print("\nvez do inimigo ⏳")
    time.sleep(0.3)    
    clear()
    print("\nvez do inimigo ⌛")
    time.sleep(0.3)    
    clear()


clear()
welcome()

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

print("\nVocê enfrentará um inimigo aleatório, prepare-se!")
time.sleep(1)
clear()

ini = (random.randint(1, 10))

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

while (vid > 0 and inivid > 0):
    playerstats()
    inistats()
    print("\nSua Vez:")
    print("1 - Atacar ⚔️")
    print("2 - Curar ✚")
    esc = int(input("Escolha: "))
    clear()
    
    critata = (random.randint(0, 10))
    critcur = (random.randint(0, 5))
    critiniata = (random.randint(0, 5))

    if esc == 1:
        inivid -= ata + critata
        
    elif esc == 2:
        vid += cur + critcur
    
    loading()
    vid-= iniata + critiniata
    
    clear()
    print(f"\nInimigo ataca com {iniata} de ataque {critiniata} de crítico")
    
    if esc == 1:
        print(f"Você ataca com {ata} de ataque {critata} de crítico")
    else:
        print(f"Você cura com {cur} e {critcur} de crítico")
            
    if inivid <=0:
        clear()
        print("\nVocê Ganhou!")
        time.sleep(3)
    elif vid <=0:
        clear()
        print("\nVocê Perdeu!")
        time.sleep(3)