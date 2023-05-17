#Centro Universitário Belas Artes
#Estruturas de Dados Não Lineares
#Prof. Lucy Mari

#Andre Toti
#RM 23106639

#Tradutor: Decimal para Binário

def decParaBin(decimal):
    pilha = [] #cria uma pilha vazia para armazenar os restos das divisōes
    while decimal > 0:
        resto = decimal % 2 #calcula o resto da divisão por 2
        pilha.append(resto) #adiciona o resto a pilha
        decimal = decimal // 2 #atualiza o valor decimal para a divisao inteira por 2

    binario = "" #cria uma string vazia para armazenar o binario
    
    while pilha:
        binario += str(pilha.pop()) #remove o ultimo elemento da pilha e adiciona a string binario
    return binario #retorna o numero binario como string

numeroDecimal = int(input("Digite um numero inteiro decimal para ser traduzido: ")) #inicio do programa
numeroBinario = decParaBin(numeroDecimal) #converte o decimal para binário
print(f'A tradução de {numeroDecimal} é: {numeroBinario}') #fim do programa exibindo o resultado

'''
Teste de Mesa:

Numéro Decimal para Teste: 1992

1. Pilha é iniciada vazia
2. Enquanto o valor decimal é maior que 0 o loop while é executado:
    1. O resto da divisão é calculado: 1992 / 2 = 0.
    2. 0 é adicionado a pilha
        Pilha = [0]
    3. O valor decimal é atualisado para a divisão inteira por 2: 1992 / 2 = 996
    4. O resto da divisão é calculado: 996 / 2 = 0.
    5. 0 é adicionado a pilha
        Pilha = [0, 0]
    6. O valor decimal é atualisado para a divisão inteira por 2: 996 / 2 = 498
    7. O resto da divisão é calculado: 498 / 2 = 0.
    8. 0 é adicionado a pilha
        Pilha = [0, 0, 0]
    9. O valor decimal é atualisado para a divisão inteira por 2: 498 / 2 = 249
    10. O resto da divisão é calculado: 249 / 2 = 1.
    11. 1 é adicionado a pilha
        Pilha = [0, 0, 0, 1]
    12. O valor decimal é atualisado para a divisão inteira por 2: 249 / 2 = 124
    13. O resto da divisão é calculado: 124 / 2 = 0.
    14. 0 é adicionado a pilha
        Pilha = [0, 0, 0, 1, 0]
    15. O valor decimal é atualisado para a divisão inteira por 2: 124 / 2 = 62
    16. O resto da divisão é calculado: 62 / 2 = 0.
    17. 0 é adicionado a pilha
        Pilha = [0, 0, 0, 1, 0, 0]
    18. O valor decimal é atualisado para a divisão inteira por 2: 62 / 2 = 31
    19. O resto da divisão é calculado: 31 / 2 = 1.
    20. 1 é adicionado a pilha
        Pilha = [0, 0, 0, 1, 0, 0, 1]
    21. O valor decimal é atualisado para a divisão inteira por 2: 31 / 2 = 15
    22. O resto da divisão é calculado: 15 / 2 = 1.
    23. 1 é adicionado a pilha
        Pilha = [0, 0, 0, 1, 0, 0, 1, 1]
    24. O valor decimal é atualisado para a divisão inteira por 2: 15 / 2 = 7
    25. O resto da divisão é calculado: 7 / 2 = 1.
    26. 1 é adicionado a pilha
        Pilha = [0, 0, 0, 1, 0, 0, 1, 1, 1]
    27. O valor decimal é atualisado para a divisão inteira por 2: 7 / 2 = 3
    28. O resto da divisão é calculado: 3 / 2 = 1.
    29. 1 é adicionado a pilha
        Pilha = [0, 0, 0, 1, 0, 0, 1, 1, 1, 1]
    30. O valor decimal é atualisado para a divisão inteira por 2: 3 / 2 = 1
    31. O resto da divisão é calculado: 1 / 2 = 1.
    31. 1 é adicionado a pilha
        Pilha = [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
3. A pilha é desempilhada para formar o numero binário corretamente:
    1. Pilha = [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
    2. Desempilhar
    3. Pilha = [0, 0, 0, 1, 0, 0, 1, 1, 1, 1]
        Binário = 1
    4. Desempilhar
    5. Pilha = [0, 0, 0, 1, 0, 0, 1, 1, 1]
        Binário = 11
    6. Desempilhar
    7. Pilha = [0, 0, 0, 1, 0, 0, 1, 1]
        Binário = 111
    8. Desempilhar
    9. Pilha = [0, 0, 0, 1, 0, 0, 1]
        Binário = 1111
    10. Desempilhar
    11. Pilha = [0, 0, 0, 1, 0, 0]
        Binário = 11111
    12. Desempilhar
    13. Pilha = [0, 0, 0, 1, 0]
        Binário = 111110
    14. Desempilhar
    15. Pilha = [0, 0, 0, 1]
        Binário = 1111100
    16. Desempilhar
    17. Pilha = [0, 0, 0]
        Binário = 11111001
    18. Desempilhar
    19. Pilha = [0, 0]
        Binário = 1111100100
    20. Desempilhar
    21. Pilha = [0]
        Binário = 1111100100
    22. Desempilhar
    23. Pilha = []
        Binário = 11111001000
    24. Desempilhar
    25. A pilha está vazia.
4. O numero Binário é apresentado = 11111001000
'''