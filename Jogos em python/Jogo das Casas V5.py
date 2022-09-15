import turtle
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
##CORES
from turtle import*
color('black', 'purple')
begin_fill()
while True:
    title("Bem vindo!")
    forward(170)
    left(100)
    if abs(pos()) < 3:
        break
end_fill()
print("O jogo das casas", "Versão 0.05 ALPHA")
print("""1. Jogar
2. Sair""")
menu=input("Coloque o numero desejado: ")
if menu=="2":
    exit(10)
##Menu


elif menu=="1":
    nome=input("Coloque seu nickname aqui: ")
    print("No inicio, a guerra assim os 4 reinos se separam por um item que todos queriam ter")
    print(f"{bcolors.OK}O pedaço da estrela{bcolors.RESET}")
    print("mais que no final ninguém ficou com ele.")
    print("Assim você o grande", nome,"vai nós salvar")
##o começo do jogo
    vida = 100
    print("Você tem", vida, "de vida")
##bestiario
print("Você pega um bestiario")
bestiario = 0
if bestiario < 1:
    print("Você não viu nem um monstro, você não tem nada nele ainda")

    print("""
Você esta na primeira vila
Explorar
Dormir""")
    reposta1=input("Fazer o que? ")
if reposta1=="dormir":
    print(f"{bcolors.FAIL}Você foi morto enquanto dormia.{bcolors.RESET}")
    vida = vida - 200
    print("Você tomou um dano critico, vida atual:", vida)
    exit(10)
##Morte 1


elif reposta1=="explorar":
    print(f"{bcolors.OK}Você achou uma roupa de couro e uma espada de madeira!{bcolors.RESET}")
    dano = 3
    armadura = 5
    print("Agora você possui", dano,"de dano e", armadura,"de armadura")
    
print("""
Assim você sai das casas principais
você encontra um monstro""")
luta1=input("Fugir ou lutar? ")
if luta1=="fugir":
    print(f"{bcolors.FAIL}Você morre ao tentar escapar{bcolors.RESET}")
    exit(10)
##Morte 2


elif luta1=="lutar":
    print(f"{bcolors.WARNING}Entrando em modo de combate{bcolors.RESET}")
lutap1=input("""
Modo de combate esta ativo
O monstro tem 100 de vida
1. atacar
2. item
3. desistir
Digite o numero escolhido: """)
if lutap1=="1":
    print("Quando você ao chegar perto do monstro surge um raio dos ceús e o atige, tirando 99999999 de vida")
    print(f"{bcolors.OK}Você venceu{bcolors.RESET}")
elif lutap1=="2":
    print("você tenta pegar ao mais é atigindo")
    print("Game Over")
    exit(10)
##Morte 3


elif lutap1=="3":
        print(f"{bcolors.FAIL}Você morre ao tentar conversar com o mosntro{bcolors.RESET}")
        exit(10)
##Morte 4

print("Você se pergunta o que aconteceu para aquele raio cair na cabeça do mostro")
bestiario = 1
if bestiario < 2:
    print("Você encontrou um slime gigante, agora em seu bestiario você tem ele registrado!")
print("Você sente uma coisa estranha ao se aproximar novamente do slime")
ver=input("Ir ver oq aconteceu? (Y) OU (N):")
if ver==("y"):
    print("você encontrou um pedaço de estrela")
    estrela = True
if ver==("n"):
    print("você segue normalmente")
    estrela = False
print("Depois de muita dificuldade você chega a segunda vila")
print("assim quando você pisa nas terras dessa vila você percebe algo diferente")
print("todos estão mortos.")
exp1=input("Explorar os restos da segunda vila? (Y) ou (N):")
if exp1=="n":
    print("você vai ao centro sem explorar nada mais é atacado é morre")
    exit(10)
elif exp1=="y":
    print("Você encotra uma espada melhor e um capacete de ferro")
    dano=15
    armadura= armadura - 5 + 10
    print("agora você tem", dano,"de dano e", armadura,"de armadura")
if estrela==True:
    print("Você vai centro e é atacado mais algo acontece, aquele pedaço de estrela ilumina todo o lugar e assim você consegue ver aqueles goblins")
    print("eles se rendem e você ganha uma armadura de ouro para mostrar a confiança dos goblins em você")
    armadura= armadura - 5 + 13
    print("+13 de armadura =", armadura)
if estrela==False:
    luta2=input("""
    Modo de combate esta ativo
    3 goblins da vila
    1. atacar
    2. item
    3. desistir
    Digite o numero escolhido: """)
    if luta2=="1":
        print("Você pega sua espada e vai para a luta contra os 3 goblins da vila, você mata todos mais perde 8 de armadura")
    armadura= armadura - 8
    if armadura<0:
        vida=vida - 3
    print("atualmente você tem", armadura,"de armadura")
    if luta2=="2":
        print("mal esperam você abrir a bolsa, e já te atacão você. Acho melhor você parar de usar essa opição")
    if luta2=="3":
        print("morto")
if estrela==True:print("Então você sai da vila, deixando seu unico pedaço de estrela")
if estrela==True:print(f"{bcolors.FAIL}-1 Pedaço de estrela{bcolors.RESET}")
elif estrela==False:print("Você sente algo estranho ao sair da vila")
print("Segundo cenario, A floresta invertida")
print("ao entrar na floresta você passa mal e gospe um pouco de sangue")
vida= vida - 5
print("atualmente você tem", vida,"de vida")
fo=input("você deseja explorar (Y) ou (N): ")
if fo=="y":
    print("você acha alguns cadaver em posição de reza")