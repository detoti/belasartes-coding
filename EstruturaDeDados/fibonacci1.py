#Centro Universitário Belas Artes
#Estruturas de Dados Não Lineares
#Prof. Lucy Mari

#Andre Toti
#RM 23106639

#Fibonacci com Recursão

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
n = dia + mes #calcula o enésimo termo com base na soma do dia e do mês

fibonacci_n = fibonacci(n) #chama a função fibonacci para calcular o enésimo termo
print("O enésimo termo da sequência de Fibonacci para n = {} é: {}".format(n, fibonacci_n))