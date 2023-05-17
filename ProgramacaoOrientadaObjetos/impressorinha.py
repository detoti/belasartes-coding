#Centro Universitário Belas Artes
#Programação Orientada a Objetos
#Prof. Marcio Calvalcante

#Andre Toti
#RM 23106639

#Impressorinha - Inimigos da HP

class impressorinha:
    def __init__(self):
        self.cartucho = 100

    def imprimir(self):
        if self.cartucho == 0:
            print('Sem tinta no cartucho. Vá ao menu para recarregar')
        else:
            impressao = input('Digite o documento a ser impresso: ')
            print(impressao)
            self.cartucho -= 20

    def nivelCartucho(self):
        print(f'Nivel do Cartucho {self.cartucho}%')

    def recarregaCartucho(self):
        self.cartucho = 100
        print(f'O Cartucho foi recarregado. Nivel atual: {self.cartucho}%')

    def easterEgg(self):
        print('♪♪♪\nInimigos da HP - Caça e Caçador\nBrilhante como\nUma estrela\nLeve e louco\nSem pressa de acabar\nE a gente nem pensa na hora\nPassa dia e noite assim\nO amor não tem que ser\nUma história\nCom princípio, meio e fim...')


InimigosDaHP = impressorinha()

while True:
    opcaoMenu = input("-= Inimigos da HP =-\nSelecione uma opção:\n1 - Imprimir\n2 - Verificar nível do cartucho\n3 - Recarregar o cartucho\n4 - Easter EGG\n0 - Sair\n")

    if opcaoMenu == "1":
        InimigosDaHP.imprimir()
    elif opcaoMenu == "2":
        InimigosDaHP.nivelCartucho()
    elif opcaoMenu == "3":
        InimigosDaHP.recarregaCartucho()
    elif opcaoMenu == "4":
        InimigosDaHP.easterEgg()
    elif opcaoMenu == "0":
        break
    else:
        print("Opção inválida")



