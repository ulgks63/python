class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
print("O jogo das casas", "Versão 0.02 ALPHA")
print("""1. Jogar
2. Configurações
3. Sair""")
menu=input("Coloque o numero desejado: ")
if menu=="2":
    print("Opção indisponivel!")
    exit(10)
elif menu=="3":
    exit(10)
elif menu=="1":
    vida = 100
    print("Você tem", vida, "de vida")
    print("""
Você esta nas primeiras casas da vila
Explorar
Dormir
    """)
    reposta1=input("Fazer o que? ")
if reposta1=="Dormir":
    print(f"{bcolors.FAIL}Você foi morto enquanto dormia.{bcolors.RESET}")
    vida = 100 - 200
    print("Você tomou um dano critico, vida atual", vida)
    exit(10)
elif reposta1=="Explorar":
    print(f"{bcolors.OK}Você achou uma roupa de couro e uma espada de madeira!{bcolors.RESET}")
    armadura = 5
    print("Aogra você possui", vida,"de vida e", armadura,"de armadura")
    dano = 3
print("""Assim você sai das casas principais
         você encontra um monstro""")
luta1=input("Fugir ou lutar? ")
if luta1=="fugir":
    print(f"{bcolors.FAIL}Você morre ao tentar escapar{bcolors.RESET}")
    exit(10)
elif luta1=="lutar":
    print(f"{bcolors.WARNING}Entrando em modo de combate{bcolors.RESET}")
    lutap1=input("""
Modo de combate esta ativo
O monstro tem 100 de vida
1. atacar
2. item
3. desistir
    """)
if lutap1=="1":
    print("Quando você ao chegar perto do monstro surge um raio dos ceús e o atige, tirando 99999999 de vida")
    print("Você venceu")
elif lutap1=="2":
    print("você tenta pegar ao mais é atigindo")
elif lutap1=="3":
        print(f"{bcolors.FAIL}Você morre ao tentar conversar com o mosntro{bcolors.RESET}")
        exit(10)    