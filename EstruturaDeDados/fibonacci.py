#Centro Universitário Belas Artes
#Estruturas de Dados Não Lineares
#Prof. Lucy Mari

#Andre Toti
#RM 23106639

#Fibonacci com Recursão

fib = int(input('Quantos números da sequencia você deseja exibir? ')) #inicio do programa
f1 = 1 #primeiro número da sequencia
f2 = 1 #segundo número da sequencia
print('{} , {}'.format(f1, f2), end='')
contador = 3 #contador para executar a recursão e reaproveitar o código
while contador <= fib: #enquanto o contador for menor ou igual ao numero de sequencias solicitadas, ele continua rodando
    f3 = f1 + f2 #calculo para formar o terceiro número da sequencia
    print(' , {}'.format(f3), end='')
    f1 = f2 #alteramos as variaveis para que o calculo continue
    f2 = f3
    contador += 1 #adicionamos 1 ao contador para que execute os calculos conforme a quantidade solicitada
print(' , Fim da sequencia solicitada.') #fim do programa
