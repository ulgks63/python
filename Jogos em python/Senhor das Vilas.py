from uuid import uuid4
from flask_principal import Identity, Need, Permission
gen_user_id = lambda: str(uuid4())
import turtle
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
#
# cores
# 
from turtle import*
color('black', 'purple')
begin_fill()
while True:
    title("Bem vindo!")
    forward(170)
    left(100)
    if abs(pos()) < 3:
        break
# Turtle
# Menu
print("Senhor das vilas", "Versão 0.01 Beta")
print("""
    1. Jogar
    2. Sair
""")
m=input("Selecione um dos números: ")
if m=="2":exit(10)
if m=="1":
    nome=input("Digite seu nickname: ")
    OgroNeed = Need('Raça', 'Ogro')
    HumanoNeed = Need('Raça', 'Humano')
RaceSelector = {
    1: OgroNeed,
    2: HumanoNeed
}
user_race = -1

while user_race == -1 and user_race not in RaceSelector.keys():

    user_race_inpt = input('''
        Select your nature:
            1. Ogro
            2. Humano
    ''')

    if user_race_inpt.isnumeric():
        user_race = int(user_race_inpt)

user_race = RaceSelector.get(user_race)
user_char = Identity(gen_user_id())
user_char.provides.add(user_race)
print("Você acorda em uma cama de palha, e percebe que ninguém foi te receber")
print("Você ouve um barulho de algo caindo.")
explo1=input("""Ir investigar
    1. Sim
    2. Não
Escolha um dos numeros: """)
if explo1=="2":
    print(f"{bcolors.FAIL}Você morreu vacilão{bcolors.RESET}")
    exit(10)
elif explo1=="1":
    print("Você vai para fora da casa, e ver muitos camponeses mortos e alguns feridos")
    print("Automaticamente você lembra da maldita guerra sem sentindo entre as duas raças")
print("Você pega um escudo um elmo e um espada e parte para acabar com essa guerra sem sentido. Você é nossa Salvação", nome)