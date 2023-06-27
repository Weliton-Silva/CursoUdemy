valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 > valor2:
    print(f'O primeiro valor {valor1} é maior')
elif valor1 < valor2:
    print(f'O segundo valor {valor2} é maior')
else:
    print('Ambos valores são iguais.')