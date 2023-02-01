# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

number = input('Informe o número: ')
number = float(number)
rounded = round(number)

if number == rounded:
    print('Inteiro')
else:
    print('Decimal')