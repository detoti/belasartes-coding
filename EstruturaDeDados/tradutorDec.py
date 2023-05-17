#Centro Universitário Belas Artes
#Estruturas de Dados Não Lineares
#Prof. Lucy Mari

#Andre Toti
#RM 23106639

#Tradutor: Binario para Decimal

def binParaDec(binario):
    fila = [] #cria uma fila vazia
    for digito in binario: #adiciona cada dígito do número binário na fila
        fila.append(int(digito))

    numeroDec = 0 #inicializa a variável com zero

    while len(fila) > 0: #processa cada dígito da fila
        digito = fila.pop(0) #remove o primeiro dígito da fila
        posicaoFila = 2 ** (len(fila)) #calcula o valor da posição correspondente
        numeroDec += digito * posicaoFila #multiplica o dígito pelo valor da posição e adiciona ao resultado
    return numeroDec

numeroBinario = input("Digite um numero inteiro decimal para ser traduzido: ") #inicio do programa
numeroDecimal = binParaDec(numeroBinario) #converte o decimal para binário
print(f'A tradução de {numeroBinario} é: {numeroDecimal}') #fim do programa exibindo o resultado

'''
Teste de Mesa:

Numéro Binario para Teste: 10110

1. A Fila vazia recebe o Numero Binário digitado: 
    fila = [1, 0, 1, 1, 0]
    numeroDec = 0

2. O metodo while é executado enquanto o tamanho da fila for maior que 0
    1. digito = fila.pop(0) = 1
    2. valor_posicao = 2 ** (len(fila)) = 2 ** 4 = 16
    3. numeroDec += digito * valor_posicao = 1 * 16 = 16
    
    4. digito = fila.pop(0) = 0
    5. valor_posicao = 2 ** (len(fila)) = 2 ** 3 = 8
    6. numeroDec += digito * valor_posicao = 0 * 8 = 0
    
    7. digito = fila.pop(0) = 1
    8. valor_posicao = 2 ** (len(fila)) = 2 ** 2 = 4
    9. numeroDec += digito * valor_posicao = 1 * 4 = 4
    
    10. digito = fila.pop(0) = 1
    11. valor_posicao = 2 ** (len(fila)) = 2 ** 1 = 2
    12. numeroDec += digito * valor_posicao = 1 * 2 = 2
    
    13. digito = fila.pop(0) = 0
    14. valor_posicao = 2 ** (len(fila)) = 2 ** 0 = 1
    15.numeroDec += digito * valor_posicao = 0 * 1 = 0

    16. Erro: fila fica vazia

3. O metodo while para pois a fila fica vazia
    retorna numeroDec = 16 + 0 + 4 + 2 + 0 = 22

4. A tradução de 10110 é: 22
'''