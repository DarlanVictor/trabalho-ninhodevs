notas = []
nota = 0
maiormedia = []
while(len(notas) < 5):
    nota = float(input("Escreva uma nota: "))
    
    if(nota <= 10 and nota >= 0):
        notas.append(nota)
        
    else:
        print("Valor invalido")


media = sum(notas) / len(notas)

for n in notas:
    if n > media:
        maiormedia.append(n)

print(f'A soma de todas as notas: {sum(notas)}')
print("A média do aluno é:", media)
print(f'Os valores maiores que a media são: {maiormedia}')

if(media >=  7):
    print ("Resultado final: APROVADO")
elif(media <=  5):
    print ("Resultado final: REPROVADO")
elif(media > 5 and media < 7):
    print("Resultado final: RECUPERAÇÃO")
else:
    print("Notas inválidas")
