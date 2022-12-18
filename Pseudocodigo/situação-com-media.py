nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
if media >=5 and media < 6:
    print('O aluno está de recuperação com media', media)
elif media < 5:
    print('O aluno foi reprovado com media', media)
else:
    print('O aluno foi aprovado com media', media)
