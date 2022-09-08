print("O jogo das casas", "Versão 0.01 ALPHA")
print("1. Jogar")
print("2. Configurações")
print("3. Sair")
menu=input("Coloque o numero desejado: ")
if menu=="2":
    print("Opção indisponivel!")
    exit(10)
if menu=="3":
    exit(100)
if menu=="1":
    vida = 100
    print ("Você tem", vida,"de vida")
    print("Você esta nas primeiras casas da vila")
    print("Explorar")
    print("Dormir")
    f=input("Fazer o que? ")
if f=="Dormir":
    print("Você foi morto enquanto dormia.")
    vida = 100 - 200
    print("Você tomou um dano critico, vida atual", vida)
    exit(10)
if f=="Explorar":
    print("Você achou uma roupa de couro e uma espada de madeira!")
    armadura = 5
    print("Aogra você possui", vida,"de vida e", armadura,"de armadura")
    dano = 3
print("Assim você sai das casas principais")
print("você encontra um monstro")
luta1=input("Fugir ou lutar? ")
if luta1=="fugir":
    print("Você morre ao tentar escapar")
    vida = vida - 100
    armadura = armadura - 5
    print("vida atual:",vida,"armadura atual:", armadura)