#Escreva um programa Python para adivinhar um número entre 1 a 9.
#Nota: O usuário é solicitado a inserir um palpite. Se o usuário adivinhar errado, o prompt aparecerá novamente até que o palpite esteja correto.
#Se o palpite for bem-sucedido, o usuário receberá um "Bem adivinhado!" mensagem e o programa será encerrado.

from random import randint
pc, jogador = randint(1,10), 0
print('Vou pensar em um número entre 1 a 9, Tente adivinhar...')

while pc != jogador:
    jogador = int(input('Digite seu palpite: '))

print('Bem adivinhado!')
