class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
##CORES


print("O jogo das casas", "Versão 0.03 ALPHA")
print("""1. Jogar
2. Configurações
3. Sair""")
menu=input("Coloque o numero desejado: ")
if menu=="2":
    print("Opção indisponivel!")
    exit(10)
elif menu=="3":
    exit(10)
##Menu


elif menu=="1":
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
Digite o numero escolhido""")
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
print("VITORIA VOCÊ SALVOU OS 5 REINOS")