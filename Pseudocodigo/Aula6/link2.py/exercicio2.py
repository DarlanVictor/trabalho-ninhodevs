temperatura = (input("Digite a temperatura: "))
tipo = temperatura[-1]
valor = int(temperatura[:-1])
convertido = 0
tipoConvertido = ""
siglaConvertido = ""


if tipo.upper() == "F":
    convertido = int(((valor - 32) * 5) / 9)
    tipoConvertido = "Celsius"
    siglaConvertido = "C"
elif tipo.upper() == "C":
    convertido = int((9 * valor) / 5 + 32)
    tipoConvertido = "Fahrenheit"
    siglaConvertido = "F"
else:
    print("Digite um temperatura válida, terminada em C se for Celsius, ou em F se for Fahrenheit")

print(f"{temperatura} convertido para {tipoConvertido} fica: {convertido}{siglaConvertido}")
