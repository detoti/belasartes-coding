#Centro Universitário Belas Artes
#Programação Orientada a Objetos
#Prof. Marcio Calvalcante

#Andre Toti
#RM 23106639

#Prova - POO - Software para Empresa de Pequeno Porte - Manutenção Eletrônica
#Desenvolver um software para computador que faça o gerenciamento dos dados, com integração entre as informaçōes necessárias.

#Trecho Desenvolvido: Controle de Estoque; Fazer lista de Compras de Componentes Eletronicos

class ListaDeComponentes:
    def __init__(self):
        self.lista = []
    
    def adicionarComponente(self, item, quantidade):
        for i in range(quantidade):
            self.lista.append(item)
    
    def contar_itens(self):
        contagem = {}
        for item in self.lista:
            contagem[item] = contagem.get(item, 0) + 1
        return contagem
    
    def adicionar_quantidade(self, item, quantidade):
        for i in range(quantidade):
            self.lista.append(item)

lista = ListaDeComponentes()

while True:
    print("\n1 - Adicionar Componente Eletrônico a Lista de Compra")
    print("2 - Imprimir lista de Compras")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o Componente: ")
        quantidade = int(input("Digite a quantidade: "))
        lista.adicionarComponente(item, quantidade)
    elif opcao == "2":
        contagem = lista.contar_itens()
        for item, quantidade in contagem.items():
            print(item, quantidade)
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")