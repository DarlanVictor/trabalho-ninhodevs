x = int(input('Digite um valor positivo maior que zero: '))
y = int(input('Digite um valor positivo maior que zero: '))
z = int(input('Digite um valor positivo maior que zero: '))
if x > y and x > z:
    print('O maior número é', x)
elif y > x and y > z:
    print('O maior número é', y)
else:
    print('O maior número é', z)
