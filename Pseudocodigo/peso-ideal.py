print('Vamos calcular o seu IMC?')
peso_ideal = float
altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo: ')
if(sexo == 'masculino'):
    peso_ideal = (72.7*altura)-58
elif(sexo == 'feminino'):
    peso_ideal = (62.1*altura)-44.7
else:
    print('Sexo indefinido')
print("O seu peso Ideal é", peso_ideal)
