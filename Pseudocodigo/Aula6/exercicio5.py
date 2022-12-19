# Escreva um programa Python para obter o menor número de uma lista
lista = []
for item in range(1,5):
    lista.append(int(input('Digite um número: ')))
print('O menor valor da lista é', (min(lista)))
