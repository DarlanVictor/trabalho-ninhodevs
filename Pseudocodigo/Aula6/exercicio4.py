#Escreva um programa em Python para obter o maior número de uma lista.
lista = []
for n in range(0,3):
    lista.append(int(input('Digite um número na lista: ')))
print('O maior número da lista é:', (max(lista)))
